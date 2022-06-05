from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.permissions import IsTeacherOrDean
from features.models import Competence, Specialization, Discipline
from testing.models import Testing, Question, Answer
from testing.serializer import TestingSerializer, AnswerSerializer, QuestionSerializer


class CreateTest(APIView):
    permission_classes = (IsTeacherOrDean,)

    def post(self, request):
        test = request.data
        serializer = TestingSerializer(data=test)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        test_uuid = str(serializer.data["uuid_testing"])
        return Response({"message": "Test succesfully created", "uuid": test_uuid}, status=status.HTTP_201_CREATED)


class UpdateTest(APIView):
    permission_classes = (IsTeacherOrDean,)

    def put(self, request):
        test = request.data
        uuid_testing = test.get("uuid_testing")
        specialization_id = test.get("specialization_id")
        discipline_id = test.get("discipline_id")
        if not uuid_testing:
            return Response({"error": "Testing not found"}, status=status.HTTP_404_NOT_FOUND)
        try:
            current_testing = Testing.objects.get(uuid_testing=uuid_testing)
        except Testing.DoesNotExist:
            return Response({"error": "Testing not found"}, status=status.HTTP_404_NOT_FOUND)
        if specialization_id:
            try:
                specialization = Specialization.objects.get(pk=specialization_id)
                current_testing.specialization = specialization
            except Specialization.DoesNotExist:
                return Response({"error": "Specialization not found"}, status=status.HTTP_404_NOT_FOUND)
        if discipline_id:
            try:
                discipline = Discipline.objects.get(pk=discipline_id)
                current_testing.discipline = discipline
            except Discipline.DoesNotExist:
                return Response({"error": "Discipline not found"}, status=status.HTTP_404_NOT_FOUND)
        current_testing.save()
        serializer = TestingSerializer(instance=current_testing, data=test, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = serializer.data
        return Response(response, status=status.HTTP_201_CREATED)


class DeleteTest(APIView):
    permission_classes = (IsTeacherOrDean,)

    def post(self, request):
        uuid_testing = request.data.get("uuid_testing")
        testing_to_delete = Testing.objects.filter(uuid_testing=uuid_testing)
        if testing_to_delete:
            testing_to_delete.first().delete()
            return Response({"message": "Test succesfully deleted"}, status=status.HTTP_200_OK)
        return Response({"message": "Nothing to delete"}, status=status.HTTP_404_NOT_FOUND)


class GetTest(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, **kwargs):
        user_status = request.user.status
        uuid_testing = kwargs.get("uuid_testing")
        testing = Testing.objects.filter(uuid_testing=uuid_testing)
        if testing:
            serializer = TestingSerializer(instance=testing.first(), context={"user_status": user_status})
            response = serializer.data
            return Response(response, status=status.HTTP_200_OK)
        return Response({"message": "Test not found"}, status=status.HTTP_404_NOT_FOUND)


class ListOfTest(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        testings = Testing.objects.all()
        serializer = TestingSerializer(instance=testings, many=True)
        response = serializer.data
        return Response(response, status=status.HTTP_200_OK)


class CreateQuestion(APIView):
    permission_classes = (IsTeacherOrDean,)

    def post(self, request):
        question = request.data
        uuid_testing = question.get("uuid_testing")
        if not uuid_testing:
            return Response({"error": "Testing not specified"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            testing = Testing.objects.get(uuid_testing=uuid_testing)
        except Testing.DoesNotExist:
            return Response({"error": "Testing not found"}, status=status.HTTP_404_NOT_FOUND)
        question["testing"] = testing.id
        serializer = QuestionSerializer(data=question)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        question = serializer.data
        return Response({"message": "Question succesfully created", "question": question}, status=status.HTTP_201_CREATED)


class UpdateQuestion(APIView):
    permission_classes = (IsTeacherOrDean,)

    def put(self, request):
        question = request.data
        uuid_question = question.get("uuid_question")
        competence_id = question.get("competence_id")
        if not uuid_question:
            return Response({"error": "Question not found"}, status=status.HTTP_404_NOT_FOUND)
        try:
            current_question = Question.objects.get(uuid_question=uuid_question)
        except Question.DoesNotExist:
            return Response({"error": "Question not found"}, status=status.HTTP_404_NOT_FOUND)
        if competence_id:
            try:
                current_question.competence = Competence.objects.get(pk=competence_id)
                current_question.save()
            except Competence.DoesNotExist:
                return Response({"error": "Competence not found"}, status=status.HTTP_404_NOT_FOUND)
        if current_question.type_answer_question != question.get("type_answer_question"):
            current_question.answer_set.all().update(correct_answer=False)
        serializer = QuestionSerializer(instance=current_question, data=question, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = serializer.data
        return Response(response, status=status.HTTP_201_CREATED)


class DeleteQuestion(APIView):
    permission_classes = (IsTeacherOrDean,)

    def post(self, request):
        uuid_question = request.data.get("uuid_question")
        question_to_delete = Question.objects.filter(uuid_question=uuid_question)
        if question_to_delete:
            question_to_delete.first().delete()
            return Response({"message": "Question succesfully deleted"}, status=status.HTTP_200_OK)
        return Response({"message": "Nothing to delete"}, status=status.HTTP_404_NOT_FOUND)


class CreateAnswer(APIView):
    permission_classes = (IsTeacherOrDean,)

    def post(self, request):
        answer = request.data
        uuid_question = answer.get("uuid_question")
        if not uuid_question:
            return Response({"error": "Question not found"}, status=status.HTTP_400_BAD_REQUEST)
        question = Question.objects.filter(uuid_question=uuid_question)
        if not question:
            return Response({"error": "Question not found"}, status=status.HTTP_404_NOT_FOUND)

        answer["question"] = question.first().id
        serializer = AnswerSerializer(data=answer)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        answer = serializer.data
        return Response({"message": "Answer succesfully created", "answer": answer}, status=status.HTTP_201_CREATED)


class UpdateAnswer(APIView):
    permission_classes = (IsTeacherOrDean,)

    def put(self, request):
        answer = request.data
        uuid_answer = answer.get("uuid_answer")
        if not uuid_answer:
            return Response({"error": "Answer not found"}, status=status.HTTP_404_NOT_FOUND)
        current_answer = Answer.objects.filter(uuid_answer=uuid_answer).first()
        if not current_answer:
            return Response({"error": "Answer not found"}, status=status.HTTP_404_NOT_FOUND)
        correct_answer = answer.get("correct_answer")
        if correct_answer is not None:
            current_answer.correct_answer = correct_answer
            current_answer.save()
        serializer = AnswerSerializer(instance=current_answer, data=answer, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = serializer.data
        return Response(response, status=status.HTTP_201_CREATED)


class DeleteAnswer(APIView):
    permission_classes = (IsTeacherOrDean,)

    def post(self, request):
        uuid_answer = request.data.get("uuid_answer")
        answer_to_delete = Answer.objects.filter(uuid_answer=uuid_answer)
        if answer_to_delete:
            answer_to_delete.first().delete()
            return Response({"message": "Answer succesfully deleted"}, status=status.HTTP_200_OK)
        return Response({"message": "Nothing to delete"}, status=status.HTTP_404_NOT_FOUND)


class LoadExcel(APIView):
    permission_classes = (IsTeacherOrDean,)

    def post(self, request):
        test_file = request.data.get("excel")
        return Response({"message": "Starting_load"}, status=status.HTTP_200_OK)


class Refor(APIView):
    def get(self, request):
        questions = Question.objects.all()
        for q in questions:
            q.reforeign()
        return Response({"message": "OK"}, status=status.HTTP_200_OK)
