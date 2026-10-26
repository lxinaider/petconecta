from django.contrib import admin

from ongs.models import Ong


class OngAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "legal_name",
        "trade_Name",
        "cnpj",
        "email",
        "phone",
        "city",
        "state",
        "description",
    )


admin.site.register(Ong)
