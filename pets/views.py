from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from pets.forms import PetForm
from pets.models import Pet


def update(request, pk=None):
    pet = Pet.objects.get(pk)
    form = PetForm(request.POST or None, request.FILES or None, instance=pet)
    if form.is_valid():
        form.save()
        return redirect("/")

    return render(request, "pets/add.html", {"form": form})


def create(request):
    form = PetForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("/")

    return render(request, "pets/add.html", {"form": form})


def list(request):
    pets = Pet.objects.all()

    return render(request, "pets/list.html", {"pets": pets})

@login_required
@require_POST
def delete(request, pk=None):
    pet = Pet.objects.get(pk)
    pet.delete()
    return redirect("home")


def detail(request, pk):
    pets = get_object_or_404(Pet, pk)
    return render(request, "pet/detail.html", {"pets": pets})
