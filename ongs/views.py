from django.shortcuts import redirect, render

from ongs.forms import OngForm
from ongs.models import Ong


def create(request):
    form = OngForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("home")

    return render(request, "ongs/create.html", {"form": form})


def delete(request, pk=None):
    ong = Ong.objects.get(pk=pk)
    ong.delete()
    return redirect("home")
