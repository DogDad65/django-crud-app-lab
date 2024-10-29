# my_app/forms.py
from django import forms
from .models import Bike, Maintenance

class BikeForm(forms.ModelForm):
    class Meta:
        model = Bike
        fields = ['brand', 'model', 'description', 'category']
        
class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = Maintenance
        fields = ['date', 'maintenance_type', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }
