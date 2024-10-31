# forms.py
from django import forms
from .models import Maintenance, Upgrade

class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = Maintenance
        fields = ['date', 'maintenance_type', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class UpgradeForm(forms.ModelForm):
    class Meta:
        model = Upgrade
        fields = ['type', 'description', 'date_installed', 'bike']
        widgets = {
            'date_installed': forms.DateInput(attrs={'type': 'date'}),
        }