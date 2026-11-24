from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from pets.forms import PetForm
from pets.models import Adoption, Pet


@login_required
def update(request, pk):
    ong = request.user.ong
    if ong is None:
        return redirect("create_ong")

    pet = get_object_or_404(Pet, pk=pk)
    form = PetForm(request.POST or None, request.FILES or None, instance=pet)
    if form.is_valid():
        form.save()
        return redirect("home_ong")

    return render(request, "pets/create.html", {"form": form})


@login_required
def create(request):
    ong = request.user.ong
    if ong is None:
        return redirect("create_ong")

    form = PetForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        pet = form.save(commit=False)
        pet.ong = ong
        pet.save()
        return redirect("home")

    return render(request, "pets/create.html", {"form": form})


def list(request):
    pets = Pet.objects.all()

    return render(request, "pets/list.html", {"pets": pets})


@login_required
@require_POST
def delete(request, pk=None):
    pet = get_object_or_404(Pet, pk=pk)

    if request.user.ong.pk == pet.ong.pk:
        pet.delete()
        return redirect("home")

    return redirect("home")


def detail(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    adoption = None
    if request.user.is_authenticated:
        adoption = Adoption.objects.filter(pet=pet, user=request.user).first()

    return render(
        request,
        "pets/detail.html",
        {"pet": pet, "adoption": adoption},
    )


@login_required
@require_POST
def request_adoption(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    adoption, created = Adoption.objects.get_or_create(pet=pet, user=request.user)

    if created:
        messages.success(request, f"Sua solicitação para adotar {pet.name} foi enviada.")
    else:
        messages.info(request, f"Você já enviou uma solicitação para adotar {pet.name}.")

    return redirect("detail_pet", pk=pet.pk)
