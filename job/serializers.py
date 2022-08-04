from rest_framework import serializers
from job.models import Category

class CategorySerializer(serializers.ModelSerializer):
    worker_count = serializers.IntegerField()
    salary_from = serializers.DecimalField(max_digits=12, decimal_places=2)
    salary_to = serializers.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        model = Category
        fields = ['title', 'worker_count']


class MainSerializer(serializers.Serializer):
    worker_count = serializers.IntegerField()
    vacancy_count = serializers.IntegerField()
    company_count = serializers.IntegerField()


