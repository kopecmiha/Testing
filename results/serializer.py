from rest_framework import serializers

from testing.serializer import AnswerSerializer, TestingSerializer
from .models import TestingResults


class ResultsSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, required=False)
    testing = TestingSerializer(required=False)

    class Meta(object):
        model = TestingResults
        fields = "result_uuid", "test_started", "test_finished", "testing", "answers", "user"
        extra_kwargs = {'result_uuid': {'read_only': True}, 'test_started': {'read_only': True}}
