from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from ongs.forms import OngForm
from ongs.models import Ong
from pets.models import Adoption
from users.models import User


@login_required
def create(request):
    if request.user.ong is not None:
        return redirect("home")

    pending_ong = Ong.objects.filter(
        created_by=request.user,
        status=Ong.Status.PENDING,
    ).first()
    if pending_ong:
        return render(
            request,
            "ongs/create.html",
            {"pending_ong": pending_ong},
        )

    form = OngForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        ong = form.save(commit=False)
        ong.status = Ong.Status.PENDING
        ong.created_by = request.user
        ong.save()
        return redirect("create_ong")

    return render(request, "ongs/create.html", {"form": form})


@login_required
def update(request, pk):
    ong = request.user.ong
    if ong is None:
        return redirect("create_ong")

    ong = get_object_or_404(Ong, pk=pk)
    form = OngForm(request.POST or None, request.FILES or None, instance=ong)
    if form.is_valid():
        form.save()
        return redirect("home_ong")

    return render(request, "ongs/create.html", {"form": form})


@login_required
@require_POST
def delete(request, pk=None):
    ong = Ong.objects.get(pk=pk)
    ong.delete()
    return redirect("home")


@login_required
@require_POST
def delete_admin(request, pk=None):
    ong = request.user.ong
    if ong is None:
        return redirect("create_ong")

    admin = get_object_or_404(User, pk=pk, ong=ong)
    if admin.pk == request.user.pk:
        messages.error(request, "Você não pode remover a si mesmo.")
        return redirect("home_ong")

    admin.ong = None
    admin.save(update_fields=["ong"])
    messages.success(request, f"{admin.name or admin.email} foi removido da ONG.")

    return redirect("home_ong")


@login_required
@require_POST
def add_admin(request):
    ong = request.user.ong
    if ong is None:
        return redirect("create_ong")

    email = request.POST.get("email", "").strip()
    admin = User.objects.filter(email__iexact=email).first()

    if not email:
        messages.error(request, "Informe o e-mail do usuário.")
    elif admin is None:
        messages.error(request, "Nenhum usuário encontrado com esse e-mail.")
    elif admin.ong_id == ong.pk:
        messages.error(request, "Esse usuário já é administrador da ONG.")
    elif admin.ong is not None:
        messages.error(request, "Esse usuário já administra outra ONG.")
    else:
        admin.ong = ong
        admin.save(update_fields=["ong"])
        messages.success(request, f"{admin.name or admin.email} foi adicionado à ONG.")

    return redirect("home_ong")


@login_required
def home(request):
    ong = request.user.ong
    if ong is None:
        return redirect("create_ong")

    pending_adoptions = Adoption.objects.filter(
        pet__ong=ong,
        status=Adoption.Status.PENDING,
    ).select_related("pet", "user")
    return render(
        request,
        "ongs/index.html",
        {"ong": ong, "pending_adoptions": pending_adoptions},
    )


@login_required
def adoption_detail(request, pk):
    ong = request.user.ong
    if ong is None:
        return redirect("create_ong")

    adoption = get_object_or_404(
        Adoption.objects.select_related("pet", "user"),
        pk=pk,
        pet__ong=ong,
    )
    return render(
        request,
        "ongs/adoption_detail.html",
        {"ong": ong, "adoption": adoption},
    )


@login_required
@require_POST
def approve_adoption(request, pk):
    ong = request.user.ong
    if ong is None:
        return redirect("create_ong")

    adoption = get_object_or_404(
        Adoption,
        pk=pk,
        pet__ong=ong,
        status=Adoption.Status.PENDING,
    )
    adoption.status = Adoption.Status.APPROVED
    adoption.save(update_fields=["status"])
    messages.success(
        request,
        f"A adoção de {adoption.pet.name} por {adoption.user.name or adoption.user.email} foi aprovada.",
    )
    return redirect("home_ong")
