from django.db import models


class ONG(models.Model):
    legal_name = models.CharField(max_length=20)
    trade_Name = models.CharField(max_length=20)
    cnpj = models.CharField(max_length=14)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2)
    description = models.CharField(max_length=150)
