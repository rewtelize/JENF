from datetimewidget.widgets import DateWidget
from django import forms
from models import User


class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['project']
        dateTimeOptions = {
            'format': 'dd/mm/yyyy',
            'autoclose': True,
            'weekStart': 1,
            'todayHighlight': True,
            'language': 'es',
        }
        widgets = {
            'birthdate': DateWidget(attrs={'id': "birthdate"}, options=dateTimeOptions, bootstrap_version=3),
        }

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

