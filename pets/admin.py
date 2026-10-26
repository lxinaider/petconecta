from django.contrib import admin

from pets.models import Pet


class PetAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "species",
        "breed",
        "description",
        "image",
        "ong",
    )


admin.site.register(Pet)
