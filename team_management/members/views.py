import json

from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

from members.models import Member
from members.utils.forms import MemberForm

# Create your views here.
def get_all_members(request):
    try:
        members = Member.objects.all().values()
        return render(
            request=request, template_name="index.html", context={"members": members}
        )
    except Exception as err:
        return HttpResponse(err)


@csrf_exempt
def get_all_members_api(request):
    try:
        members = serializers.serialize("json", Member.objects.all())
        return HttpResponse(members)
    except Exception as err:
        return HttpResponse(err)


@csrf_exempt
def get_member_by_id_api(request, id: int):
    try:
        member = serializers.serialize("json", [Member.objects.get(id=id)])
        return HttpResponse(member)
    except Exception as err:
        return HttpResponse(err)


def add_member(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            valid = Member.is_valid_request(form.cleaned_data)
            if not valid[0]:
                return HttpResponse(valid[1])

            try:
                phone_number = form.cleaned_data.get("phone_number")

                if Member.objects.filter(phone_number=phone_number).exists():
                    return HttpResponse(f"Member already exists!")

                new_member = Member(**form.cleaned_data)
                new_member.save()
                return redirect("/members/")
            except Exception as err:
                return HttpResponse(err)
        else:
            return HttpResponse("Invalid form")
    else:
        return render(
            request=request,
            template_name="modify.html",
            context={"form": MemberForm, "mode": "add"},
        )


@csrf_exempt
def add_member_api(request):
    if request.method == "POST":
        request_body = json.loads(request.body)
        valid = Member.is_valid_request(request_body)
        if not valid[0]:
            return HttpResponse(valid[1])

        try:
            phone_number = request_body.get("phone_number")

            if Member.objects.filter(phone_number=phone_number).exists():
                return HttpResponse(f"Member already exists!")

            new_member = Member(
                first_name=request_body.get("first_name"),
                last_name=request_body.get("last_name"),
                phone_number=phone_number,
                email=request_body.get("email"),
                role=request_body.get("role", "regular"),
            )
            new_member.save()
            return HttpResponse(f"Member {new_member} was saved successfully")
        except Exception as err:
            return HttpResponse(err)
    else:
        return HttpResponseNotAllowed(["POST"])


def edit_member(request, id: int):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            valid = Member.is_valid_request(form.cleaned_data)
            if not valid[0]:
                return HttpResponse(valid[1])

            try:
                phone_number = form.cleaned_data.get("phone_number")

                if not Member.objects.filter(phone_number=phone_number).exists():
                    return HttpResponse(f"Member does not exist!")

                member = Member.objects.get(id=id)
                for key, value in form.cleaned_data.items():
                    setattr(member, key, value)
                member.save()
                return redirect("/members/")
            except Exception as err:
                return HttpResponse(err)
        else:
            return HttpResponse("Invalid form")
    else:
        try:
            member = Member.objects.get(id=id)
            form = MemberForm(
                initial={
                    "first_name": member.first_name,
                    "last_name": member.last_name,
                    "phone_number": member.phone_number,
                    "email": member.email,
                    "role": member.role,
                }
            )
            return render(
                request=request,
                template_name="modify.html",
                context={"form": form, "mode": "edit", "url": f"/members/edit/{id}/"},
            )
        except Exception as err:
            return HttpResponse(err)


@csrf_exempt
def edit_member_api(request, id: int):
    if request.method == "PUT":
        try:
            request_body = json.loads(request.body)
            valid = Member.is_valid_request(request_body)
            if not valid[0]:
                return HttpResponse(valid[1])

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
def delete_member_api(request, id: int):
    try:
        member_to_delete = Member.objects.get(id=id)
        member_to_delete.delete()
        return HttpResponse(f"Member deleted!")
    except Exception as err:
        return HttpResponse(err)
