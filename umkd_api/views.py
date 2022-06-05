from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from features.models import Competence
from umkd_api.serializer import DesktopCompetenceSerializer


class ListOfCompetences(APIView):
    def get(self, request):
        competences = Competence.objects.all()
        serializer = DesktopCompetenceSerializer(instance=competences, many=True)
        response = serializer.data
        return Response(response, status=status.HTTP_200_OK)
