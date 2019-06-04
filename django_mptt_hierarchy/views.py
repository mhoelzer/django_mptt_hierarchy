from django.shortcuts import render, reverse, HttpResponseRedirect
from django_mptt_hierarchy.models import File
from django.views import View


def homepage(request):
    return render(request, "files.html", {"files": File.objects.all()})
