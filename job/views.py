from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, views
from job.serializers import MainSerializer, CategorySerializer
from job.models import Vacancy, Worker
from django.db.models import Count, Avg, Q
from django.db import models
from job.models import Company
from job.models import Category
from helpers.pagination import CustomPagination

# Create your views here.
class MainView(views.APIView):
    serializer_class = MainSerializer
    
    def get(self, request, format=None):
        worker_count = Worker.objects.count()
        vacancy_count = Vacancy.objects.count()
        company_count = Company.objects.count()
        content = {'vacancy_count:' : vacancy_count, 'company_count' : company_count, 'worker_count' : worker_count}
        return Response(content)


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.annotate(worker_count=Count('categories'))
    serializer_class = CategorySerializer
    pagination_class = CustomPagination


