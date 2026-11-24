from django.contrib import admin

from ongs.models import Ong


class OngAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "legal_name",
        "trade_name",
        "cnpj",
        "email",
        "phone",
        "city",
        "state",
        "description",
        "status",
        "created_by",
    )
    list_filter = ("status", "state")
    search_fields = ("legal_name", "trade_name", "cnpj", "email")


admin.site.register(Ong)
