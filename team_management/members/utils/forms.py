from django.forms import ModelForm, TextInput, RadioSelect, ChoiceField
from members.models import Member, ROLES


class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = "__all__"
        widgets = {
            "first_name": TextInput(attrs={"placeholder": "First name"}),
            "last_name": TextInput(attrs={"placeholder": "Last name"}),
            "phone_number": TextInput(attrs={"placeholder": "Phone number"}),
            "email": TextInput(attrs={"placeholder": "Email"}),
            "role": RadioSelect(choices=ROLES),
        }
