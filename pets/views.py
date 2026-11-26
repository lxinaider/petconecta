from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError, transaction
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.http import require_POST

from pets.forms import AdopterProfileForm, AdoptionRequestForm, PetForm
from pets.models import AdopterProfile, AdoptionRequest, Pet


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
        pet.archived = timezone.now()
        pet.save(update_fields=["archived"])
        messages.info(request, f"{pet.name} foi arquivado")
        return redirect("home")

    return redirect("home")


def detail(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    adoption = None
    if request.user.is_authenticated:
        adoption = AdoptionRequest.objects.filter(pet=pet, adopter=request.user).first()

    return render(
        request,
        "pets/detail.html",
        {"pet": pet, "adoption": adoption},
    )


@login_required
def request_adoption(request, pk):
    pet = get_object_or_404(Pet, pk=pk)

    if AdoptionRequest.objects.filter(
        pet=pet,
        adopter=request.user,
        status__in=[
            AdoptionRequest.AdoptionStatus.PENDING,
            AdoptionRequest.AdoptionStatus.IN_REVIEW,
            AdoptionRequest.AdoptionStatus.APPROVED,
        ],
    ).exists():
        messages.info(request, f"Você já enviou uma solicitação para adotar {pet.name}.")
        return redirect("detail_pet", pk=pet.pk)

    profile = AdopterProfile.objects.filter(user=request.user).first()
    profile_form = AdopterProfileForm(
        request.POST or None, instance=profile, prefix="profile"
    )
    request_form = AdoptionRequestForm(request.POST or None, prefix="request")

    if request.method == "POST":
        if all([profile_form.is_valid(), request_form.is_valid()]):
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()

            adoption = request_form.save(commit=False)
            adoption.pet = pet
            adoption.adopter = request.user
            adoption.accepted_terms_at = timezone.now()
            adoption.save()
            messages.success(
                request, f"Sua solicitação para adotar {pet.name} foi enviada."
            )

            return redirect("detail_pet", pk=pet.pk)

    return render(
        request,
        "pets/adoption.html",
        {"pet": pet, "profile_form": profile_form, "request_form": request_form},
    )
