from dataclasses import field
from rest_framework import serializers
from job.models import Category

class CategorySerializer(serializers.ModelSerializer):
    worker_count = serializers.IntegerField()
    class Meta:
        model = Category
        fields = ['title', 'worker_count']


class MainSerializer(serializers.Serializer):
    worker_count = serializers.IntegerField()
    vacancy_count = serializers.IntegerField()
    company_count = serializers.IntegerField()


