from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import render, redirect, get_object_or_404
from .form import CreateNewTask, CreateNewProject

# Create your views here.
def index(request):
    title = "Bienvenido a Django APP"
    return render (request, 'index.html', {
        'title':title
    })


def about(request):
    username = 'Hidelberg'
    return render (request, 'about.html', {
        'username' : username
    })


def hello(request, username):
    print(username)
    return HttpResponse('<h1>Hello %s</h1>' %username)


def projects(request):
    #Projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render (request, 'Projects/projects.html', {
        'projects': projects
    })

def task(request):
    #task = Task.objects.get(title=title)
    tasks = Task.objects.all()
    return render (request, 'tasks/tasks.html', {
        'tasks': tasks
    })

def create_task(request):
    if request.method == 'POST':
        form = CreateNewTask(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            Task.objects.create(title=title, description=description, project_id=2)
            return redirect('Tasks')  # Asegúrate de que esta URL está configurada en tus urls.py
    else:
        form = CreateNewTask()

    return render(request, 'tasks/create_task.html', {'form': form})


def create_project(request):
    if request.method == 'POST':
        form = CreateNewProject(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            Project.objects.create(name=name)
            return redirect('projects')
    else:
        form = CreateNewProject()

    return render(request, 'Projects/create_project.html', {'form': form})

    
def project_detail (request, id):
    project = Project.objects.get(id=id)
    tasks = Task.objects.filter(project_id=id)
    get_object_or_404(Project, id=id)
    print(project)
    return render(request, 'Projects/detail.html', {
        'project' : project,
        'tasks': tasks
    })