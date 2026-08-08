from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexViwe.as_view(), name = 'index')
]
