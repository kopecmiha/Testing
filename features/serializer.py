from rest_framework import serializers
from .models import Specialization, Competence, Discipline


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Specialization
        fields = "id", "title", "code"
        extra_kwargs = {'id': {'read_only': True}}


class CompetenceSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Competence
        fields = "id", "code"
        extra_kwargs = {'id': {'read_only': True}}


class DisciplineSerializer(serializers.ModelSerializer):
    competences = CompetenceSerializer(required=False, many=True)
    specialization = SpecializationSerializer(required=False)

    class Meta(object):
        model = Discipline
        fields = "id", "title", "competences", "specialization"
        extra_kwargs = {'id': {'read_only': True}, 'competences': {'read_only': True}, 'specialization': {'read_only': True}}
