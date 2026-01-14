from django.contrib import admin
from .models import Patient


# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", "phone", "blood_group", "gender", "is_active"]
    list_filter = ["is_active", "gender", "blood_group"]
    search_fields = ["first_name", "last_name"]
    fieldsets = (
        ("Informations personnelles", {
            'fields': ('photo', 'first_name', 'last_name', 'date_of_birth', 'gender')
        }),
        ("Contact", {
            'fields': ('phone', 'email', 'address_1', 'address_2', 'code_zone', 'city', 'country')
        }),
        ("Contact d'urgence", {
            'fields': ('emergency_contact_name', 'emergency_contact_phone')
        }),
        ("Informations médicales", {
            'fields': ('blood_group', 'allergies', 'chronic_diseases', 'current_treatments')
        }),
        ("Assurance", {
            'fields': ('insurance_name',)  # ou insurance_number si vous l'avez
        }),
        ("Statut", {
            'fields': ('is_active',)
        }),
    )

admin.site.register(Patient, PatientAdmin)