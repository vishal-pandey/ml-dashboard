from django import forms
from dashboard.models import Dataset
from django.contrib.auth.models import User

class DatasetForm(forms.ModelForm):
     class Meta():
         model = Dataset
         fields = ('dataset', )