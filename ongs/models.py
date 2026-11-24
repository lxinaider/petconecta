from django.conf import settings
from django.db import models


class Ong(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "Pendente"
        APPROVED = "approved", "Aprovada"
        REJECTED = "rejected", "Recusada"

    legal_name = models.CharField(max_length=20)
    trade_name = models.CharField(max_length=20)
    cnpj = models.CharField(max_length=14)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2)
    description = models.CharField(max_length=150)
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.PENDING,
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="ong_requests",
    )
    image = models.ImageField(
        upload_to="ongs/",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.legal_name
