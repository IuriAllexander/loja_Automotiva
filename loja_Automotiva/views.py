from django.shortcuts import render
#from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def home(request):
    # Render takes: request, template path, and optional context
    return render(request, "home/index.html")