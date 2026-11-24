from django.db import models


class Pet(models.Model):
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


class Adoption(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "Pendente"
        APPROVED = "approved", "Aprovada"
        REJECTED = "rejected", "Recusada"

    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE,
        related_name="adoptions",
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="adoptions",
    )
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.PENDING,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["pet", "user"],
                name="unique_pet_adoption_request",
            )
        ]
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user} - {self.pet}"
