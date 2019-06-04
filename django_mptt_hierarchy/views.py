from django.shortcuts import render, reverse, HttpResponseRedirect
from django_mptt_hierarchy.models import File
from django_mptt_hierarchy.forms import FileAddForm
from django.views import View


def homepage_view(request):
    return render(request, "homepage.html", {"files": File.objects.all()})


def file_add_view(request):
    pass
    html = "add_file.html"
    form = None
    if request.method == "POST":
        form = FileAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            File.objects.create(
                name=data["name"],
                parent=data["parent"]
            )
        return HttpResponseRedirect(reverse('homepage'))
    else:
        form = FileAddForm()
    return render(request, html, {"form": form})