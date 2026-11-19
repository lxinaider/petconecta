from django.urls import path

from . import views

urlpatterns = [
    path("create/", views.create, name="create_ong"),
    path("update/<pk>", views.update, name="update_ong"),
    path("delete/", views.delete, name="delete_ong"),
    path("delete/admin/<int:pk>", views.delete_admin, name="delete_admin"),
    path("", views.home, name="home_ong"),
]
