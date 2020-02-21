from django.contrib.auth import get_user_model
from django.db import models

class Attendance(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    punch_in = models.DateTimeField(auto_now=False, auto_now_add=False)
    punch_out = models.DateTimeField(auto_now=False, auto_now_add=False)