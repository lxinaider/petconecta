from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from ongs.models import Ong
from pets.models import Pet


def home(request):
    pets = Pet.objects.filter(ong__status=Ong.Status.APPROVED, archived__isnull=True)
    query = request.GET.get("q", "").strip()

    if query:
        pets = pets.filter(name__icontains=query)

    return render(request, "index.html", {"pets": pets, "query": query})


@login_required
def admin(request):
    if not request.user.is_staff:
        return HttpResponse(status=403)

    pending_ongs = Ong.objects.filter(status=Ong.Status.PENDING).order_by("-id")
    return render(request, "admin_panel/index.html", {"pending_ongs": pending_ongs})


@login_required
@require_POST
def approve_ong(request, pk):
    if not request.user.is_staff:
        return HttpResponse(status=403)

    ong = get_object_or_404(Ong, pk=pk, status=Ong.Status.PENDING)
    ong.status = Ong.Status.APPROVED
    ong.save(update_fields=["status"])
    if ong.created_by is not None:
        ong.created_by.ong = ong
        ong.created_by.save(update_fields=["ong"])
    return redirect("admin_panel")


@login_required
@require_POST
def reject_ong(request, pk):
    if not request.user.is_staff:
        return HttpResponse(status=403)

    ong = get_object_or_404(Ong, pk=pk, status=Ong.Status.PENDING)
    ong.status = Ong.Status.REJECTED
    ong.save(update_fields=["status"])
    return redirect("admin_panel")
