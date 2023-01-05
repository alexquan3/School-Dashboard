from django.shortcuts import render
from .models import Classes, Tasks
from .forms import ClassForm, TaskForm
# Create your views here.
def home(request):
    return render(request, 'main/home.html', {})

def classes(request):
    classes = Classes.objects.all()
    #current_user = request.user
    for c in classes:
        print(c)
    return render(request, 'main/classes.html', {'classes': classes})