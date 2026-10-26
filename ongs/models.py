from django.conf import settings
from django.db import models


class Ong(models.Model):
    admins = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="managed_ongs",
        blank=True,
    )

    legal_name = models.CharField(max_length=20)
    trade_Name = models.CharField(max_length=20)
    cnpj = models.CharField(max_length=14)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2)
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.legal_name
