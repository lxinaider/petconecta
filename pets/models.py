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
