from django import forms
from .models import LostItem

class LostItemForm(forms.ModelForm):
    class Meta:
        model = LostItem
        fields = ['name', 'description', 'lost_date', 'image', 'location']
        widgets = {
            'lost_date': forms.DateInput(attrs={'type': 'date'}),
        }
