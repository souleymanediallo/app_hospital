from django.db import models


# Create your models here.
GENDER_CHOICES = [
    ("M", "Male"),
    ("F", "Female"),
]

BLOOD_GROUP_CHOICES = [
    ("A+", "A+"), ("A-", "A-"),
    ("B+", "B+"), ("B-", "B-"),
    ("AB+", "AB+"), ("AB-", "AB-"),
    ("O+", "O+"), ("O-", "O-"),
]


class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="patients_photos/", blank=True, null=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True, unique=True)
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100, blank=True, null=True)
    code_zone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    social_security_number = models.CharField(max_length=100, blank=True)
    insurance_number = models.CharField(max_length=50, blank=True)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES, blank=True, null=True)
    allergies = models.TextField(blank=True)
    chronic_diseases = models.TextField(blank=True)
    current_treatments = models.TextField(blank=True)
    emergency_contact_name = models.CharField(max_length=100, blank=True)
    emergency_contact_phone = models.CharField(max_length=15, blank=True, null=True)
    insurance_name = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"
