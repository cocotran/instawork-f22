from django.urls import path

from . import views
from members.views import (
    MemberListView,
    MemberCreateView,
    MemberUpdateView,
    MemberDeleteView,
)


urlpatterns = [
    path("", MemberListView.as_view(), name="member-list"),
    path("add/", MemberCreateView.as_view(), name="member-add"),
    path("edit/<int:pk>/", MemberUpdateView.as_view(), name="member-edit"),
    path("delete/<int:pk>/", MemberDeleteView.as_view(), name="member-delete"),
]
