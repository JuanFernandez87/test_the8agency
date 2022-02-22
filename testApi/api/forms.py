from django import forms

class CreateForm(forms.Form):
    name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    country = forms.CharField(max_length=30)
    phone = forms.CharField(max_length=30)
    job = forms.CharField(max_length=30)
    