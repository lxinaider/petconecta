from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from pets.models import Pet


def home(request):
    pets = Pet.objects.all()

    return render(request, "index.html", {"pets": pets})


@login_required
def admin(request):
    if not request.user.is_staff:
        return HttpResponse(status=403)

    return render(request, "admin/index.html")
