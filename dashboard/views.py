from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from application.models import Application

@login_required
def index(request):
    applications = Application.objects.filter(created_by=request.user)

    return render(request, 'dashboard/index.html', {
        'applications': applications,
    })