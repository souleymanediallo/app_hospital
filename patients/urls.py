from django.urls import path
from . import views

app_name = "patients"

urlpatterns = [
    path('', views.home, name="index"),
    path('patients', views.patient_list, name="patient_list"),
    path('patients/<int:pk>', views.patient_detail, name="patient_detail"),
    path("new", views.patient_form, name="patient_new"),
]