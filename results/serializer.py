from rest_framework import serializers

from testing.models import Answer, Question
from testing.serializer import TestingSerializer, QuestionSerializer
from .models import TestingSession, UserAnswers


class ResultAnswerSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Answer
        fields = "text", "uuid_answer", "correct_answer", "question"
        extra_kwargs = {'uuid_answer': {'read_only': True}}


class ResultQuestionUUIDSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Question
        fields = "uuid_question",
        extra_kwargs = {'uuid_question': {'read_only': True}}


class UserAnswersSerializer(serializers.ModelSerializer):
    def _question(self, obj):
        return obj.question.uuid_question

    question_uuid = serializers.SerializerMethodField("_question")
    answers = ResultAnswerSerializer(many=True, required=False)

    class Meta(object):
        model = UserAnswers
        fields = "question_uuid", "answers",


class ResultsSerializer(serializers.ModelSerializer):
    testing = TestingSerializer(required=False)
    useranswers_set = UserAnswersSerializer(many=True, required=False)

    class Meta(object):
        model = TestingSession
        fields = "session_uuid", "test_started", "test_finished", "testing", "user", "useranswers_set"
        extra_kwargs = {'session_uuid': {'read_only': True}, 'test_started': {'read_only': True}}
