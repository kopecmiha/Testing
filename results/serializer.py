from rest_framework import serializers

from testing.models import Answer
from testing.serializer import AnswerSerializer, TestingSerializer
from .models import TestingSession


class ResultAnswerSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Answer
        fields = "text", "uuid_answer", "correct_answer", "question"
        extra_kwargs = {'uuid_answer': {'read_only': True}}


class ResultsSerializer(serializers.ModelSerializer):
    answers = ResultAnswerSerializer(many=True, required=False)
    testing = TestingSerializer(required=False)

    class Meta(object):
        model = TestingSession
        fields = "result_uuid", "test_started", "test_finished", "testing", "answers", "user"
        extra_kwargs = {'result_uuid': {'read_only': True}, 'test_started': {'read_only': True}}
