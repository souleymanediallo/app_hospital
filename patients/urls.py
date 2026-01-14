from django.urls import path
from . import views

app_name = "patients"

urlpatterns = [
    path('', views.home, name="index"),
    path('patients', views.patient_list, name="patient_list"),
]