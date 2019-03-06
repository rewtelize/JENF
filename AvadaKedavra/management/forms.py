from django import forms
from models import User
import time


class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['project']

        widgets = {
            'residence': forms.TextInput(attrs={'placeholder': 'City where the user live'})
        }

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        self.fields['birthdate'].input_formats = ['%d/%m/%Y']
        self.fields['birthdate'].initial = time.strftime("%d/%m/%Y")
