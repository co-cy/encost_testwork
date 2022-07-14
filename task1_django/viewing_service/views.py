from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from .forms import SearchForm
from .models import Durations


def index(request: WSGIRequest):
    list_dur = None
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            print(form.to_dict())
            list_dur = Durations.objects.filter(**form.to_dict())
    else:
        form = SearchForm()

    return render(request, 'name.html', {"form": form, "list_duration": list_dur})


# Create your views here.
