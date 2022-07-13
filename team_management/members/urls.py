from django.urls import path

from . import views
from members.views import GetAllMembersView, AddMemberView, EditMemberView, DeleteMemberView


urlpatterns = [
    path("", GetAllMembersView.as_view()),
    path("add/", AddMemberView.as_view()),
    path("edit/<int:id>/", EditMemberView.as_view()),
    path("delete/<int:id>/", DeleteMemberView.as_view()),
    path("api/", views.get_all_members_api),
    path("api/member/<int:id>/", views.get_member_by_id_api),
    path("api/add/", views.add_member_api),
    path("api/edit/<int:id>/", views.edit_member_api),
    path("api/delete/<int:id>/", views.delete_member_api),
]
