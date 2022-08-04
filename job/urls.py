from django.urls import path
from job.views import MainView, CategoryListView

urlpatterns=[
    path('main/', MainView.as_view()),
    path('category/', CategoryListView.as_view()),
]