from django.shortcuts import render
from .models import Proyecto

# Create your views here.
def index(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'proyectos/index.html', {'proyectos': proyectos})
