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
        fields = "id", "description", "code"
        extra_kwargs = {'id': {'read_only': True}}


class DisciplineSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Discipline
        fields = "id", "title",
        extra_kwargs = {'id': {'read_only': True}}
