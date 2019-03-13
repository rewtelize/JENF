# coding=utf-8
from django import forms
from django.contrib.auth.models import User as UserAdmin
from models import User, Organization
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


class OrganizationCreateForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(OrganizationCreateForm, self).__init__(*args, **kwargs)


class UserAdminUpdateForm(forms.ModelForm):
    class Meta:
        model = UserAdmin
        fields = ['first_name', 'last_name', 'username', 'email']

    def __init__(self, *args, **kwargs):
        super(UserAdminUpdateForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ""
