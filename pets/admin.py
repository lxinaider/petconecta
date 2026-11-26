from django.contrib import admin

from pets.models import AdopterProfile, AdoptionRequest, Pet


class PetAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "species",
        "breed",
        "description",
        "image",
        "ong",
    )

class AdopterProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "birth_date",
        "cpf",
        "zip_code",
        "address",
        "city",
        "state",
        "housing",
        "is_rented",
        "allows_pets",
        "has_protection",
        "household_size",
        "has_children",
        "other_pets",
        "experience",
    )

class AdoptionRequestAdmin(admin.ModelAdmin):
    list_display = (
        "pet",
        "adopter",
        "status",
        "motivation",
        "hours_alone",
        "household_agrees",
        "accepted_terms_at",
    )


admin.site.register(AdoptionRequest)
admin.site.register(AdopterProfile)
admin.site.register(Pet)
