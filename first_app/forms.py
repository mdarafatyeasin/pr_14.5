from django import forms
from .models import MyModel

class add_input(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = '__all__'