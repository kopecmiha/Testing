from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.permissions import IsTeacherOrDean
from testing.models import Testing, Question, Answer
from testing.serializer import TestingSerializer, AnswerSerializer, QuestionSerializer


class CreateTest(APIView):
    permission_classes = (IsTeacherOrDean,)

    def post(self, request):
        test = request.data
        serializer = TestingSerializer(data=test)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Test succesfully created"}, status=status.HTTP_201_CREATED)


class UpdateTest(APIView):
    permission_classes = (IsTeacherOrDean,)

    def put(self, request):
        test = request.data
        uuid_testing = test.get("uuid_testing")
        if not uuid_testing:
            return Response({"error": "Testing not found"}, status=status.HTTP_404_NOT_FOUND)
        current_testing = Testing.objects.filter(uuid_testing=uuid_testing)
        if not current_testing:
            return Response({"error": "Testing not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = TestingSerializer(instance=current_testing.first(), data=test, partial=True)
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
        return Response({"message": "Question succesfully created"}, status=status.HTTP_201_CREATED)


class UpdateQuestion(APIView):
    permission_classes = (IsTeacherOrDean,)

    def put(self, request):
        question = request.data
        uuid_question = question.get("uuid_question")
        if not uuid_question:
            return Response({"error": "Question not found"}, status=status.HTTP_404_NOT_FOUND)
        try:
            current_question = Question.objects.get(uuid_question=uuid_question)
        except Question.DoesNotExist:
            return Response({"error": "Question not found"}, status=status.HTTP_404_NOT_FOUND)
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
        return Response({"message": "Answer succesfully created"}, status=status.HTTP_201_CREATED)


class UpdateAnswer(APIView):
    permission_classes = (IsTeacherOrDean,)

    def put(self, request):
        answer = request.data
        uuid_answer = answer.get("uuid_answer")
        if not uuid_answer:
            return Response({"error": "Answer not found"}, status=status.HTTP_404_NOT_FOUND)
        current_answer = Answer.objects.filter(uuid_answer=uuid_answer)
        if not current_answer:
            return Response({"error": "Answer not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = AnswerSerializer(instance=current_answer.first(), data=answer, partial=True)
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