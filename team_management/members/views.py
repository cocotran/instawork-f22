import json

from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from members.models import Member

# Create your views here.
@csrf_exempt
def get_all_members(request):
    try:
        members = Member.objects.all()
        return HttpResponse(members)
    except Exception as err:
        return HttpResponse(err)


@csrf_exempt
def get_member_by_id(request, id: int):
    try:
        member = Member.objects.get(id=id)
        return HttpResponse(member)
    except Exception as err:
        return HttpResponse(err)


@csrf_exempt
def add_member(request):
    if request.method == "POST":
        request_body = json.loads(request.body)
        # Make sure all info is filled
        required_fields = ["first_name", "last_name", "phone_number", "email"]
        for field in required_fields:
            if request_body.get(field, "") == "":
                return HttpResponse(f"Missing value for {field}")

        # TODO: validate all fields
        try:
            phone_number = request_body.get("phone_number")
            email = request_body.get("email")

            if Member.objects.filter(phone_number=phone_number).exists():
                return HttpResponse(f"Member already exists!")

            new_member = Member(
                first_name=request_body.get("first_name"),
                last_name=request_body.get("last_name"),
                phone_number=phone_number,
                email=email,
                role=request_body.get("role", "regular"),
            )
            new_member.save()
            return HttpResponse(f"Member {new_member} was saved successfully")
        except Exception as err:
            return HttpResponse(err)
    else:
        return HttpResponseNotAllowed(["POST"])


@csrf_exempt
def edit_member(request, id: int):
    if request.method == "PUT":
        try:
            request_body = json.loads(request.body)
            member = Member.objects.get(id=id)
            for key, value in request_body.items():
                setattr(member, key, value)
            member.save()
            return HttpResponse(member)
        except Exception as err:
            return HttpResponse(err)
    else:
        return HttpResponseNotAllowed(["PUT"])


@csrf_exempt
def delete_member(request, id: int):
    try:
        member_to_delete = Member.objects.get(id=id)
        member_to_delete.delete()
        return HttpResponse(f"Member deleted!")
    except Exception as err:
        return HttpResponse(err)
