from rest_framework import serializers

from features.serializer import CompetenceSerializer, DisciplineSerializer, SpecializationSerializer
from .models import Testing, Question, Answer


class AnswerSerializer(serializers.ModelSerializer):

    def _correct_answer(self, obj):
        user_status = self.context.get("user_status")
        if user_status == "STUDENT":
            return None
        return obj.correct_answer

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
        fields = "text", "type_answer_question", "uuid_question", "answers", "testing", "competence"
        extra_kwargs = {'uuid_question': {'read_only': True},
                        'image': {'read_only': True},
                        'answers': {'read_only': True},
                        'testing': {'write_only': True},
                        'competence': {'read_only': True}
                        }


class TestingSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, required=False)
    specialization = SpecializationSerializer(required=False)
    discipline = DisciplineSerializer(required=False)

    class Meta(object):
        model = Testing
        fields = "title", "answer_time", "uuid_testing", "questions", "specialization", "discipline"
        extra_kwargs = {'uuid_testing': {'read_only': True}, 'questions': {'read_only': True},
                        'specialization': {'read_only': True}, 'discipline': {'read_only': True}}
