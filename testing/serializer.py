from rest_framework import serializers

from features.serializer import CompetenceSerializer, DisciplineSerializer, SpecializationSerializer
from .models import Testing, Question, Answer


class AnswerSerializer(serializers.ModelSerializer):

    def _correct_answer(self, obj):
        mode = self.context.get("mode")
        if mode:
            return obj.correct_answer
        return False

    correct_answer = serializers.SerializerMethodField("_correct_answer")

    class Meta(object):
        model = Answer
        fields = "text", "uuid_answer", "correct_answer", "question"
        extra_kwargs = {'uuid_answer': {'read_only': True}, 'question': {'write_only': True}}


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, required=False)
    competence = CompetenceSerializer(required=False)

    class Meta(object):
        model = Question
        fields = "text", "type_answer_question", "uuid_question", "answers", "testing_array", "competence"
        extra_kwargs = {'uuid_question': {'read_only': True},
                        'image': {'read_only': True},
                        'answers': {'read_only': True},
                        'testing_array': {'write_only': True},
                        'competence': {'read_only': True}
                        }


class TestingSerializer(serializers.ModelSerializer):
    specialization = SpecializationSerializer(required=False)
    questions = QuestionSerializer(many=True, required=False)

    class Meta(object):
        model = Testing
        fields = "title", "answer_time", "uuid_testing", "questions", "specialization"
        extra_kwargs = {'uuid_testing': {'read_only': True}, 'questions': {'read_only': True}}


class TestingSerializerList(serializers.ModelSerializer):
    specialization = SpecializationSerializer(required=False)

    class Meta(object):
        model = Testing
        fields = "title", "answer_time", "uuid_testing", "specialization"
        extra_kwargs = {'uuid_testing': {'read_only': True}}
