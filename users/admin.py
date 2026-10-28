from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *(UserAdmin.fieldsets or ()),
        ("Additional information", {"fields": ("phone", "ong")}),
    )

    add_fieldsets = (
        *(UserAdmin.add_fieldsets or ()),
        ("Additional information", {"fields": ("phone", "ong")}),
    )

    list_display = (
        "username",
        "email",
        "phone",
        "is_staff",
        "is_active",
    )
