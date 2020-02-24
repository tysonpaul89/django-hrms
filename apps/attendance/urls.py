from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='attendance/attendance.html'), name='attendance'),
    path('clock-in-status', views.get_current_clock_status, name='clock-in-status'),
    path('clock-user', views.clock_user, name='clock-user'),
]
