from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Application
from .forms import NewApplicationForm, EditApplicationForm

def message(request, pk):
  application = get_object_or_404(Application, pk=pk)
  related_applications = Application.objects.filter(appuniname=application.appuniname).exclude(pk=pk)[0:3]

  return render(request, 'application/message.html', {
    'application': application,
    'related_applications': related_applications
  })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewApplicationForm(request.POST, request.FILES)

        if form.is_valid():
            application = form.save(commit=False)
            application.created_by = request.user
            application.save()

            return redirect('application:message', pk=application.id)
    else:
        form = NewApplicationForm()

    return render(request, 'application/form.html', {
        'form': form,
        'title': 'New application',
    })

@login_required
def edit(request, pk):
    application = get_object_or_404(Application, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditApplicationForm(request.POST, request.FILES, instance=application)

        if form.is_valid():
            form.save()

            return redirect('application:message', pk=application.id)
    else:
        form = EditApplicationForm(instance=application)

    return render(request, 'application/form.html', {
        'form': form,
        'title': 'Edit application',
    })

@login_required
def delete(request, pk):
    application = get_object_or_404(Application, pk=pk, created_by=request.user)
    application.delete()

    return redirect('dashboard:index')