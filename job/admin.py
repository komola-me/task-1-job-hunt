from django.contrib import admin
from job.models import Company, Category, Vacancy, Worker

# Register your models here.
admin.site.register(Company)
admin.site.register(Category)
admin.site.register(Vacancy)
admin.site.register(Worker)
