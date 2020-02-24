from django.contrib import admin
from .models import Attendance


class AttendanceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Attendance, AttendanceAdmin)