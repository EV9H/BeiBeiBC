from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    context = {
        'username' : "test"
    }
    return render(request, "beiciApp/index.html", context)