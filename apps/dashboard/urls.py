from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(TemplateView.as_view(template_name='dashboard/dashboard.html')), name='dashboard')
]