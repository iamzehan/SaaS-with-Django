from django.urls import path

from . import views

urlpatterns = [
    path("my_profile", views.my_profile_view, name="my_profile"),
    path("lists", views.profile_list_view),
    path("<str:username>/", views.profile_detail_view),
]
