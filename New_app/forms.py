from django import forms
from New_app import models

# create your forms Here

class TodoForm(forms.ModelForm):
    class Meta:
        model = models.Todo_content
        fields = '__all__'
