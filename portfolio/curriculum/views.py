from django.shortcuts import render
from .models import CV

# Create your views here.
def landing(request):
    entradas = CV.objects.all()
    return render(request, "curriculum/landing.html", {"entradas": entradas})
