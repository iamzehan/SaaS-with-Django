from django.urls import path

from . import views

urlpatterns = [
    path("lists", views.profile_list_view),
    path("<str:username>/", views.profile_detail_view),
]
