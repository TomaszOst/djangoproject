from django import forms
from .models import Client, ClientInfo
from django.forms import ModelForm

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = "__all__"

        labels = {
            'first_name':"Customer first name",
            'last_name':"Customer last name",
            'age':'Customer age'
        }

        error_messages = {
            'age':{
                'min_value':"Min value is 0",
                'max_value':"Max value is 120"
            }
        }

class ClientForm2(ModelForm):
    class Meta:
        model = ClientInfo
        fields = "__all__"

        labels = {
            'zip_code':"Customer zip code",
            'address':"Customer address",
            'marital_status':"Married?",
            'amount_of_income':"Customer average income",
            'date_of_commencement_of_work':"Customer date of commencement of work",
            'number_of_dependent_children':"Number of dependent children",
        }