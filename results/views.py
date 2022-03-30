from datetime import datetime, timedelta

from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from results.models import TestingSession, UserAnswers
from testing.models import Testing


class StartTesting(APIView):
    permission_classes = (AllowAny,)

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
    permission_classes = (AllowAny,)

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
    permission_classes = (AllowAny,)

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
        question = test.question_set.filter(uuid_question=question_uuid)
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
