from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("pets", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Adoption",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("status", models.CharField(choices=[("pending", "Pendente"), ("approved", "Aprovada"), ("rejected", "Recusada")], default="pending", max_length=10)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("pet", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="adoptions", to="pets.pet")),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="adoptions", to=settings.AUTH_USER_MODEL)),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
        migrations.AddConstraint(
            model_name="adoption",
            constraint=models.UniqueConstraint(fields=("pet", "user"), name="unique_pet_adoption_request"),
        ),
    ]
