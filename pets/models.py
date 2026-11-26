from django.db import models

from users.models import User


class Pet(models.Model):
    class Status(models.TextChoices):
        AVAILABLE = "available", "Disponível"
        RESERVED = "reserved", "Em processo"
        ADOPTED = "adopted", "Adotado"

    archived = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=Status, default=Status.AVAILABLE)
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=20)
    breed = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to="pets/",
        blank=True,
        null=True,
    )

    ong = models.ForeignKey(
        "ongs.Ong",
        on_delete=models.CASCADE,
        related_name="pets",
    )

    def __str__(self):
        return self.name


class AdopterProfile(models.Model):
    class Housing(models.TextChoices):
        HOUSE = "house", "Casa"
        APARTMENT = "apartment", "Apartamento"

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="adopter_profile",
    )
    birth_date = models.DateField()
    cpf = models.CharField(max_length=11)
    zip_code = models.CharField(max_length=8)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    housing = models.CharField(max_length=10, choices=Housing)
    is_rented = models.BooleanField(default=False)
    allows_pets = models.BooleanField(null=True, blank=True)
    has_protection = models.BooleanField(default=False)
    household_size = models.PositiveSmallIntegerField()
    has_children = models.BooleanField(default=False)
    other_pets = models.TextField(blank=True)
    experience = models.TextField(blank=True)


class AdoptionRequest(models.Model):
    class AdoptionStatus(models.TextChoices):
        PENDING = "pending", "Pendente"
        IN_REVIEW = "in_review", "Em análise"
        APPROVED = "approved", "Aprovado"
        REJECTED = "rejected", "Recusado"
        CANCELED = "canceled", "Cancelado"
        COMPLETED = "completed", "Concluído"

    pet = models.ForeignKey(
        "pets.Pet", on_delete=models.PROTECT, related_name="adoption_requests"
    )
    adopter = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="adoption_requests",
    )
    status = models.CharField(
        max_length=12, choices=AdoptionStatus, default=AdoptionStatus.PENDING
    )

    motivation = models.TextField()
    hours_alone = models.PositiveSmallIntegerField()
    household_agrees = models.BooleanField()
    accepted_terms_at = models.DateTimeField()

    reviewed_by = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="reviewed_adoptions",
    )
    reviewed_at = models.DateTimeField(null=True, blank=True)
    decision_note = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
