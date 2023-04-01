from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=20)
    description = forms.CharField(widget=forms.Textarea)
    location = forms.CharField(max_length=100)
