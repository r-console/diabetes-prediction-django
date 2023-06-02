from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('pred/', views.PredictData),
]
