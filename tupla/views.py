from django.shortcuts import render
from .models import Project

# Create your views here.
def tecnologia(request):

    projetos = Project.objects.all()

    return render(request, 'tupla/tecnologia.html', context={'project_list': projetos})