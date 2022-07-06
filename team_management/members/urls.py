from django.urls import path

from . import views


urlpatterns = [
    path("", views.get_all_members),
    path("api/", views.get_all_members_api),
    path("api/member/<int:id>/", views.get_member_by_id_api),
    path("add/", views.add_member),
    path("api/add/", views.add_member_api),
    path("api/edit/<int:id>/", views.edit_member_api),
    path("api/delete/<int:id>/", views.delete_member_api),
]
