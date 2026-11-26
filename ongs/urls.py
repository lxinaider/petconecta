from django.urls import path

from . import views

urlpatterns = [
    path("create/", views.create, name="create_ong"),
    path("update/<pk>", views.update, name="update_ong"),
    path("delete/", views.delete, name="delete_ong"),
    path("delete/admin/<int:pk>", views.delete_admin, name="delete_admin"),
    path("add/admin/", views.add_admin, name="add_admin"),
    path("adoptions/<int:pk>/", views.adoption_detail, name="adoption_detail"),
    path(
        "adoptions/<int:pk>/approve/", views.approve_adoption, name="approve_adoption"
    ),
    path(
        "detail/adoptions/",
        views.detailed_adoption_view,
        name="detailed_adoption_view",
    ),
    path("", views.home, name="home_ong"),
]
