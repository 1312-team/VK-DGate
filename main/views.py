from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from .forms import GatesForm

# Create your views here.


def about(request):
    return render(request, "about_us.html")


def index(request):
    return render(request, "index.html")


def thanks(request):
    return render(request, "thanks.html")


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

@login_required
def home(request):
    return render(request, 'core/home.html')