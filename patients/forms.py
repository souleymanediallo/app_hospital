from django import forms
from .models import Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            "first_name",
            "last_name",
            "photo",
            "date_of_birth",
            "gender",
            "phone",
            "email",
            "address_1",
            "address_2",
            "code_zone",
            "city",
            "country",
            "social_security_number",
            "insurance_number",
            "blood_group",
            "allergies",
            "chronic_diseases",
            "current_treatments",
            "emergency_contact_name",
            "emergency_contact_phone",
            "insurance_name",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
