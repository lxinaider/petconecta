from django.urls import path

from . import views

urlpatterns = [
    path("update/", views.update, name="update_pet"),
    path("create/", views.create, name="create_pet"),
    path("list/", views.list, name="list_pet"),
    path("delete/", views.delete, name="delete_pet"),
    path("detail/<pk>", views.detail, name="detail_pet"),
]
