from django.urls import path
from . import views # nokta aynı hiyerarşide olduğunu gösteriyor


urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
]
