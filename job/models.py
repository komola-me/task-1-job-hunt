from django.db import models
from helpers.models import BaseModel
from common.models import User

# Create your models here.
class Category(BaseModel):
    title = models.CharField(max_length=255)
    # annotate: salary, number of workers


class Company(BaseModel):
    title = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='companies')


class Worker(BaseModel):
    full_name = models.CharField(max_length=128)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='workers')
    
    salary_from = models.DecimalField(max_digits=12, decimal_places=2)
    salary_to = models.DecimalField(max_digits=12, decimal_places=2)

    category = models.OneToOneField(Category, on_delete=models.CASCADE, related_name='categories')


class Vacancy(BaseModel):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Worker, on_delete=models.CASCADE, related_name='vacancies')
    
