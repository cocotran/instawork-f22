from django.urls import path

from . import views


urlpatterns = [
    path("/", views.get_all_members),
    path("<int:id>/", views.get_member_by_id),
    path("add/", views.add_member),
    path("edit/<int:id>/", views.edit_member),
    path("delete/<int:id>/", views.delete_member),
]
