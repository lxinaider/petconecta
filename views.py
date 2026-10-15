from django.shortcuts import redirect, render

from ongs.forms import OngForm
from ongs.models import ONG

def create(request):
    form = OngForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, 'ongs/create.html', { 'form' : form })

def delete(request, pk=None):
    ong = ONG.objects.get(pk=pk)
    ong.delete()
    return redirect('/')