from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("explore/", views.explore, name="explore"),
    path("language/<slug:slug>/", views.language, name="language")
]
