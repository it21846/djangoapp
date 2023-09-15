from django.urls import path

from . import views

app_name = 'application'

urlpatterns = [
  path('new/', views.new, name='new'),
  path('<int:pk>/', views.message, name='message'),
  path('<int:pk>/delete', views.delete, name='delete'),
  path('<int:pk>/edit', views.edit, name='edit'),
]