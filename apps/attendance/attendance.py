from .models import Attendance

class AttendanceDL():
    def __init__(self, *args, **kwargs):
        pass

    def get_attendance_by_user(self, user_id):
        """Method gets the given user is Clocked In or Out.

        Args:
            user_id: User object identifier.

        Returns:
            list of contiaing Attendance model instaces of the given user.
        """
        return Attendance.objects.filter(user_id=user_id)

    def clock_in_user(self, user_id, status):
        """Method add a new entry in the Attendance table to mark user in or out.

        Args:
            user_id: User object identifier.

        Returns:
            list of contiaing Attendance model instaces of the given user.
        """
        return Attendance.objects.create(
            user_id=user_id,
            status=status
        )