from datetime import datetime

from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from results.models import TestingSession
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


class UserAnswer(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        user = request.user
        session_uuid = request.data.get("session_uuid")
        try:
            session = TestingSession.objects.get(session_uuid=session_uuid, user=user)
        except TestingSession.DoesNotExist:
            return Response({"error": "Session not found"}, status=status.HTTP_404_NOT_FOUND)
        test = session.testing
        test_started = session.test_started
        answer_time = datetime.now()
        test_time = test.answer_time
        question_uuid = request.data.get("question_uuid")
        question = test.question_set.filter(uuid_question=question_uuid)
        if question:
            question = question.first()
        else:
            return Response({"error": "Question not found"}, status=status.HTTP_404_NOT_FOUND)
        answers_uuids = request.data.get("answers_uuids")
        print()
        answers = question.answer_set.filter(uuid_answer__in=answers_uuids)
        print(answers)
        if not answers:
            return Response({"error": "Answers not found"}, status=status.HTTP_404_NOT_FOUND)
        print(answer_time-test_started)
        return Response({"message": "Result appended"}, status=status.HTTP_200_OK)
