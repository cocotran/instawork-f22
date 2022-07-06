from audioop import maxpp
from django import forms


class MemberForm(forms.Form):
    first_name = forms.CharField(max_length=64, label='Your first name')
    last_name = forms.CharField(max_length=64, label='Your last name')
    phone_number = forms.CharField(max_length=10, label='Your phone number')
    email = forms.EmailField(label='Your email address')