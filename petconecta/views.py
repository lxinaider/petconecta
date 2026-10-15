from django.shortcuts import render


def home(request):
    return render(request, "adopt/page.html")
