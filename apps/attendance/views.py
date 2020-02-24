from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from .attendance import AttendanceDL


@login_required
def get_current_clock_status(request):
    """Function to check whether the current user is Clocked In or Out.

    Args:
        request: HttpRequest object.

    Returns:
        JsonResponse object.
    """
    response = {}
    try:
        # Gets the latest attendance entry
        attendance = AttendanceDL().get_attendance_by_user(user_id=request.user.id)
        attendance = attendance.order_by('-clock_time')[0]
        if attendance.status:
            response['clockIn'] = True
        else:
            response['clockIn'] = False
    except IndexError:
        response['clockIn'] = False
    return JsonResponse(response)

@login_required
def clock_user(request):
    """Function to Clocked In or Out as user.

    Args:
        request: HttpRequest object.

    Returns:
        JsonResponse object.
    """
    response = {}

    try:
        if request.method == 'GET':
            clock_status = int(request.GET.get('status'))

            if clock_status == 1:
                attendance = AttendanceDL().clock_in_user(user_id=request.user.id, status=True)
            elif clock_status == 0:
                attendance =  AttendanceDL().clock_in_user(user_id=request.user.id, status=False)

            if attendance.pk:
                response['status'] = True
    except (ValueError, AttributeError) as err:
        response['error'] = 'Invalid Clock Status!'

    return JsonResponse(response)
