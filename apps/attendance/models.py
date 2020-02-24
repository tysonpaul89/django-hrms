from django.contrib.auth import get_user_model
from django.db import models

class Attendance(models.Model):
    """Model for storing attendance data.

    Attributes:
        user: ForeignKey Mapping field to store the current user_id.
        status: Filed to identify Clock In/Out status. True - for Clock In and False - for Clock Out.
        clock_time: Time at which the clock In/Out occurred.
    """
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    status = models.BooleanField(default=False) # True - Clock In, False - Clock Out
    clock_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.status == 1:
            return 'Clock In: @' + self.clock_time.strftime('%Y-%m-%d %H:%M:%S')
        elif self.status == 0:
            return 'Clock Out: @' + self.clock_time.strftime('%Y-%m-%d %H:%M:%S')
        else:
            return 'Unknown Status @' + self.clock_time.strftime('%Y-%m-%d %H:%M:%S')
