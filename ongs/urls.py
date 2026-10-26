from django.urls import path

from . import views

urlpatterns = [
    path("create/", views.create, name="create_ong"),
    path("delete/", views.delete, name="delete_ong"),
]
