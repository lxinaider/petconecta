from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from ongs.forms import OngForm
from ongs.models import Ong
from users.models import User


@login_required
def create(request):
    if request.user.ong is not None:
        return redirect("home")

    form = OngForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        ong = form.save()
        request.user.ong = ong
        request.user.save(update_fields=["ong"])
        return redirect("home")

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
    ong = Ong.objects.get(pk=request.user.ong_id)
    admin = User.objects.get(pk=pk, ong=ong)
    admin.ong = None
    admin.save(update_fields=["ong"])

    return redirect("home_ong")


@login_required
def home(request):
    ong = request.user.ong
    if ong is None:
        return redirect("create_ong")

    return render(request, "ongs/index.html", {"ong": ong})
