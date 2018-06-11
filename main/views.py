from django.shortcuts import render
from django.shortcuts import redirect

from .forms import GatesForm
from .models import Gate
from django.http import Http404

# Create your views here.


def about(request):
    return render(request, "about_us.html")


def index(request):
    return render(request, "index.html")


def thanks(request):
    cur_link = Gate.objects.count()
    return render(request, "thanks.html", {'cur_link' : cur_link})


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
    return render(request, 'new_dgate.html', {'form' : form})


def gate_id(request, iden):
    try:
        iden = int(iden)
    except ValueError:
        raise Http404()

    sel_obj=Gate.objects.get(pk = iden)
    descr=sel_obj.description
    link=sel_obj.link
    return render(request,'gate_id.html',{"descr" : descr, "link" : link})
