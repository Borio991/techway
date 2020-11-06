from django.shortcuts import render, redirect, get_object_or_404
from .models import Project
from .forms import ProjectForm


def create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': ProjectForm}
    return render(request, 'main/create.html', context)


def view(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'main/view-projects.html', context)


def view_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'GET':
        form = ProjectForm(instance=project)
        context = {'form': form, 'project': project}
        return render(request, 'main/view_project.html', context)
