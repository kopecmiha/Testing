from django.shortcuts import render
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response

from .models import Specialization, Competence, Discipline
from .serializer import SpecializationSerializer, DisciplineSerializer, CompetenceSerializer


class SpecializationViewSet(viewsets.ViewSet):
    def list(self, request):
        result = Specialization.objects.all()
        serializer = SpecializationSerializer(result, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = SpecializationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        try:
            result = Specialization.objects.get(pk=pk)
        except Specialization.DoesNotExist:
            return Response({"message": "Specialization not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = SpecializationSerializer(result)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        try:
            result = Specialization.objects.get(pk=pk)
        except Specialization.DoesNotExist:
            return Response({"message": "Specialization not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = SpecializationSerializer(instance=result, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        try:
            result = Specialization.objects.get(pk=pk)
        except Specialization.DoesNotExist:
            return Response({"message": "Specialization not found"}, status=status.HTTP_404_NOT_FOUND)
        result.delete()
        return Response('Specialization deleted', status=status.HTTP_200_OK)


class CompetenceViewSet(viewsets.ViewSet):
    def list(self, request):
        result = Competence.objects.all()
        serializer = CompetenceSerializer(result, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = CompetenceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        try:
            result = Competence.objects.get(pk=pk)
        except Competence.DoesNotExist:
            return Response({"message": "Competence not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CompetenceSerializer(result)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        try:
            result = Competence.objects.get(pk=pk)
        except Competence.DoesNotExist:
            return Response({"message": "Competence not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CompetenceSerializer(instance=result, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        try:
            result = Competence.objects.get(pk=pk)
        except Competence.DoesNotExist:
            return Response({"message": "Competence not found"}, status=status.HTTP_404_NOT_FOUND)
        result.delete()
        return Response('Competence deleted', status=status.HTTP_200_OK)


class DisciplineViewSet(viewsets.ViewSet):
    def list(self, request):
        result = Discipline.objects.all()
        serializer = DisciplineSerializer(result, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        data = request.data
        competences = []
        specialization_id = data.get("specialization_id")
        if specialization_id is not None:
            try:
                data["specialization"] = Specialization.objects.get(pk=specialization_id)
                del data["specialization_id"]
            except Specialization.DoesNotExist:
                return Response({"error": "Specialization not found"}, status=status.HTTP_404_NOT_FOUND)
        competences_ids = request.data.get("competences_ids")
        if competences_ids is not None:
            competences = Competence.objects.filter(pk__in=competences_ids)
            del request.data["competences_ids"]
        discipline = Discipline.objects.create(**request.data)
        for competence in competences:
            discipline.competences.add(competence)
            discipline.save()
        serializer = DisciplineSerializer(instance=discipline)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        try:
            result = Discipline.objects.get(pk=pk)
        except Discipline.DoesNotExist:
            return Response({"message": "Discipline not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = DisciplineSerializer(result)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        data = request.data
        specialization_id = data.get("specialization_id")
        competences_ids = request.data.get("competences_ids")
        try:
            result = Discipline.objects.get(pk=pk)
            if specialization_id is not None:
                try:
                    result.specialization = Specialization.objects.get(pk=specialization_id)
                except Specialization.DoesNotExist:
                    return Response({"error": "Specialization not found"}, status=status.HTTP_404_NOT_FOUND)
            if competences_ids is not None:
                competences = Competence.objects.filter(pk__in=competences_ids)
                result.competences.clear()
                for competence in competences:
                    result.competences.add(competence)
                    result.save()
        except Discipline.DoesNotExist:
            return Response({"message": "Discipline not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = DisciplineSerializer(instance=result, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        try:
            result = Discipline.objects.get(pk=pk)
        except Discipline.DoesNotExist:
            return Response({"message": "Discipline not found"}, status=status.HTTP_404_NOT_FOUND)
        result.delete()
        return Response('Discipline deleted', status=status.HTTP_200_OK)
