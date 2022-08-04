from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, views
from job.serializers import MainSerializer
from job.models import Vacancy, Worker
from django.db.models import Count, Avg, Q

from job.models import Company

# Create your views here.
class MainView(views.APIView):
    serializer_class = MainSerializer
    
    def get(self, request, format=None):
        worker_count = Worker.objects.count()
        vacancy_count = Vacancy.objects.count()
        company_count = Company.objects.count()
        content = {'vacancy_count:' : vacancy_count, 'company_count' : company_count, 'worker_count' : worker_count}
        return Response(content)


