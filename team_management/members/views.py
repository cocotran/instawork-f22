from django.http import HttpResponse
from django.shortcuts import render

from models import Member

# Create your views here.
def get_all_members(request):
    members = Member.objects.all()
    return HttpResponse(members)


def get_member_by_id(request, id: int):
    member = Member.objects.get(id=id)
    return HttpResponse(member)


def add_member(request):
    # Make sure all info is filled
    required_fields = ['first_name', 'last_name', 'phone_number', 'email']
    for field in required_fields:
        if request.body.get(field, "") == "":
            return f"Missing value for {field}"

    # TODO: validate all fields

    try:
        new_member = Member(
            first_name = request.body.get("first_name"),
            last_name = request.body.get("last_name"),
            phone_number = request.body.get("phone_number"),
            email = request.body.get("email"),
            role = request.body.get("role")
        )
        new_member.save()
        return f"Member {new_member} was saved successfully"
    except Exception as err:
        return HttpResponse(err)


def edit_member(request):
    pass


def delete_member(request):
    pass