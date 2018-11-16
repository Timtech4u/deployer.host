from django import forms
from .models import Deploy

class DeployForm(forms.ModelForm):

    class Meta:
        model = Deploy
        fields = '__all__'