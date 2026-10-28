from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from .forms import LoginForm, RegisterForm


class CustomLoginView(LoginView):
    template_name = "users/login.html"
    authentication_form = LoginForm
    redirect_authenticated_user = True


def register(request):
    if request.user.is_authenticated:
        return redirect("home")

    form = RegisterForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("login")

    return render(request, "users/register.html", {"form": form})


@login_required
@require_POST
def delete(request):
    user = request.user
    logout(request)
    user.delete()
    return redirect("home")
