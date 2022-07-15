from django import forms


class MemberForm(forms.Form):
    first_name = forms.CharField(
        max_length=64,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "First name"}),
    )
    last_name = forms.CharField(
        max_length=64,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Last name"}),
    )
    phone_number = forms.CharField(
        max_length=10,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Phone number"}),
    )
    email = forms.EmailField(
        required=True, widget=forms.TextInput(attrs={"placeholder": "Email"})
    )
    role = forms.ChoiceField(
        choices=[
            ("regular", "Regular - Can't delete members"),
            ("admin", "Admin - Can delete members"),
        ],
        widget=forms.RadioSelect(attrs={"class": "role"}),
        initial=("regular", "Regular - Can't delete members"),
    )
