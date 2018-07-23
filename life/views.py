from django.shortcuts import render
from django.core import serializers
from life.models import *

def index(request):
    all_tasks = Task.objects.all()
    all_tags = Tag.objects.all()
    return render(request, 'life/index.html', {"tasks": all_tasks, "tags": all_tags})
  
#def tags(request):
    #all_tags = Tag.objects.all()
    #return render(request, 'life/index.html', {"tags": all_tags})