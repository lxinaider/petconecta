from django.shortcuts import render

from pets.models import Pet


def home(request):
    pets = Pet.objects.all()

    return render(request, "index.html", {"pets": pets})
