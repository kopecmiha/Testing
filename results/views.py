from datetime import datetime, timedelta
from io import BytesIO

from django.db.models import Q
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.permissions import IsTeacherOrDean
from results.models import TestingSession, UserAnswers
from results.serializer import ResultsSerializer
from testing.models import Testing, Question
import xlsxwriter


class StartTesting(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        test = request.data.get("test_uuid")
        user = request.user
        test_started = datetime.now()
        try:
            test = Testing.objects.get(uuid_testing=test)
        except Testing.DoesNotExist:
            return Response({"error": "Test not found"}, status=status.HTTP_404_NOT_FOUND)
        test_session = TestingSession.objects.create(testing=test, user=user, test_started=test_started)
        return Response({"message": "Test session created", "session_uuid": test_session.session_uuid},
                        status=status.HTTP_201_CREATED)


class FinishTesting(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        session_uuid = request.data.get("session_uuid")
        user = request.user
        try:
            session = TestingSession.objects.get(session_uuid=session_uuid, user=user)
        except TestingSession.DoesNotExist:
            return Response({"error": "Session not found"}, status=status.HTTP_404_NOT_FOUND)
        session.test_finished = datetime.now()
        session.save()
        return Response({"message": "Test session finished"}, status=status.HTTP_200_OK)


class UserAnswer(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        user = request.user
        session_uuid = request.data.get("session_uuid")
        try:
            session = TestingSession.objects.get(session_uuid=session_uuid, user=user)
        except TestingSession.DoesNotExist:
            return Response({"error": "Session not found"}, status=status.HTTP_404_NOT_FOUND)
        if session.test_finished is not None:
            return Response({"error": "Testing finished"}, status=status.HTTP_400_BAD_REQUEST)
        test = session.testing
        test_started = session.test_started.timestamp()
        answer_time = datetime.now().timestamp()
        diff = timedelta(seconds=answer_time - test_started)
        test_time = timedelta(seconds=test.answer_time)
        if test_time < diff:
            return Response({"error": "Time is over"}, status=status.HTTP_400_BAD_REQUEST)
        question_uuid = request.data.get("question_uuid")
        question = Question.objects.filter(uuid_question=question_uuid)
        if question:
            question = question.first()
        else:
            return Response({"error": "Question not found"}, status=status.HTTP_404_NOT_FOUND)
        answers_uuids = request.data.get("answers_uuids")
        answers = question.answer_set.filter(uuid_answer__in=answers_uuids)
        if not answers:
            return Response({"error": "Answers not found"}, status=status.HTTP_404_NOT_FOUND)
        user_answer, created = UserAnswers.objects.get_or_create(session=session, question=question)
        user_answer.answers.set(answers)
        user_answer.save()
        return Response({"message": "Result appended"}, status=status.HTTP_200_OK)


class GetSelfAnswers(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, **kwargs):
        user = request.user
        uuid_testing = kwargs.get("uuid_testing")
        session_results = TestingSession.objects.filter(Q(user=user) & Q(testing__uuid_testing=uuid_testing))
        serializer = ResultsSerializer(instance=session_results, many=True)
        response = serializer.data
        return Response(response, status=status.HTTP_200_OK)


class AnswersToExcel(APIView):
    permission_classes = (IsTeacherOrDean,)

    def get(self, request, **kwargs):
        uuid_testing = kwargs.get("uuid_testing")
        testing_name = Testing.objects.get(uuid_testing=uuid_testing).title
        testing_results = TestingSession.objects.filter(testing__uuid_testing=uuid_testing)
        questions = Question.objects.filter(testing_array__icontains=uuid_testing).values_list("text", flat=True)
        result_questions = {}
        for column, question in enumerate(list(questions)):
            result_questions.update({question: column + 1})
        result_questions.update({"Тест пройден на": len(result_questions) + 1})
        last_column = len(result_questions)
        # workbook = xlsxwriter.Workbook(BytesIO(), {"in_memory": True})
        workbook = xlsxwriter.Workbook('%s.xlsx' % testing_name)
        worksheet = workbook.add_worksheet()
        string_format = workbook.add_format({"border": 1, "border_color": "black"})
        percent_format = workbook.add_format({'num_format': '0.00"%"', "border": 1, "border_color": "black"})
        worksheet.set_column(0, 0, 45)
        worksheet.set_column(last_column, last_column, 20)
        for question, column_index in result_questions.items():
            worksheet.write(
                0, column_index, question, string_format
            )
        for row_index, testing_result in enumerate(testing_results):
            user_last_name = testing_result.user.last_name
            worksheet.write(
                row_index + 1, 0, user_last_name, string_format
            )
            user_answers = testing_result.useranswers_set.all()
            for user_answer in user_answers:
                question = user_answer.question.text
                answers = user_answer.answers.values_list("correct_answer", flat=True)
                answers = int(any(list(answers)))
                worksheet.write(
                    row_index + 1, result_questions[question], answers, string_format
                )
                formula_finish_cell = chr(65+last_column-1)
                formula_text = "=SUM(B%s:%s%s)/%s*100" % (row_index + 2, formula_finish_cell, row_index + 2, last_column-1)
                worksheet.write_formula(
                    row_index + 1, last_column, formula_text, percent_format
                )
        worksheet.write(
            len(testing_results)+1, 0, "Средний процент прохождения теста группой", string_format
        )
        formula_result_finish_cell = chr(65 + last_column - 1)
        formula_result_text = "=SUM(B1:%s%s)/%s*100" % (formula_result_finish_cell, len(testing_results) + 1, last_column - 1)
        worksheet.write_formula(
            len(testing_results) + 1, 1, formula_result_text, percent_format
        )
        workbook.close()
        return Response("Ok", status=status.HTTP_200_OK)
