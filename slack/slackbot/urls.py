from django.urls import path
from . import views


urlpatterns = [
    path('', views.slack, name='slack'),
]
