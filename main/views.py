from django.shortcuts import render
from django.shortcuts import redirect

from .forms import GatesForm
from .models import Gate

# Create your views here.


def about(request):
    return render(request, "about_us.html")


def index(request):
    return render(request, "index.html")


def thanks(request):
    return render(request, "thanks.html")


def gate(request):
    desc = Gate.objects.all()
    return render(request, "gate.html", locals())


def new_dgate(request):
    if request.method == "POST":
        form = GatesForm(request.POST)
        if form.is_valid():
            gate = form.save(commit=False)
            gate.save()
            return redirect(thanks)
    else:
        form = GatesForm()
    return render(request, 'new_dgate.html', {'form': form})
