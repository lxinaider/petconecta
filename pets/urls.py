from django.urls import path

from . import views

urlpatterns = [
    path("update/<pk>", views.update, name="update_pet"),
    path("create/", views.create, name="create_pet"),
    path("list/", views.list, name="list_pet"),
    path("delete/<pk>", views.delete, name="delete_pet"),
    path("<int:pk>/adopt/", views.request_adoption, name="request_adoption"),
    path("<pk>/", views.detail, name="detail_pet"),
]
