from django.shortcuts import render, get_object_or_404
from datetime import date

from .models import Patient

# Create your views here.
def home(request):
    patients = Patient.objects.all()
    context = {
        "patients": patients,
        "total_patients": Patient.total_patients(),
        "total_active": Patient.total_active(),
        "total_male": Patient.total_male(),
        "total_female": Patient.total_female(),
    }
    return render(request, "patients/index.html", context)


def patient_list(request):
    patients = Patient.objects.filter(is_active=True).order_by("last_name")
    context = {
        "patients": patients
    }
    return render(request, "patients/patient_list.html", context)


def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)

    today = date.today()
    age = today.year - patient.date_of_birth.year

    if (today.month, today.day) < (patient.date_of_birth.month, patient.date_of_birth.day):
        age -= 1

    context = {
        "patient" : patient,
        "age": age,
    }

    return render(request, "patients/patient_detail.html", context)



