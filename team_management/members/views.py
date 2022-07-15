import json

from django.views.generic import View, ListView, CreateView, DeleteView, UpdateView
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.urls import reverse_lazy

from members.models import Member
from members.utils.forms import MemberForm

# Create your views here.
class MemberListView(ListView):
    model = Member
    template_name = "index.html"
    context_object_name = "members"


class MemberCreateView(CreateView):
    model = Member
    form_class = MemberForm
    template_name = "modify.html"
    extra_context = {"mode": "add"}
    success_url = reverse_lazy("member-list")


class MemberUpdateView(UpdateView):
    model = Member
    form_class = MemberForm
    template_name = "modify.html"
    extra_context = {"mode": "edit"}
    success_url = reverse_lazy("member-list")

    def get(self, request, *args, **kwargs):
        if not Member.objects.filter(pk=self.kwargs.get("pk")).exists():
            return redirect("/")
        return super(MemberUpdateView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["id"] = self.object.id
        return context


class MemberDeleteView(DeleteView):
    model = Member
    success_url = reverse_lazy("member-list")
