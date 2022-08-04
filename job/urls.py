from django.urls import path
from job.views import MainView

urlpatterns=[
    path('main/', MainView.as_view()),
]