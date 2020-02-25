# from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from .models import Attendance


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
        attendance = Attendance.objects.filter(user_id=request.user.pk).order_by('-clock_time')[0]
        if attendance.status:
            response['clockIn'] = True
        else:
            response['clockIn'] = False
    except (IndexError, AttributeError):
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
                status = True
            else:
                status = False

            attendance = Attendance.objects.create(
                user_id=request.user.pk,
                status=status
            )

            if attendance.pk:
                response['status'] = True
    except (ValueError, AttributeError):
        response['error'] = 'Invalid Clock Status!'

    return JsonResponse(response)

@login_required
def get_last_clocked_data(request):
    """Function to Clocked In or Out as user.

    Args:
        request: HttpRequest object.

    Returns:
        JsonResponse object.
    """
    response = {}
    try:
        # Gets the latest attendance entry
        attendance = Attendance.objects.filter(user_id=request.user.pk, status=True).order_by('-clock_time')
        latestClockedIn = attendance[0].clock_time if attendance else None
        latestClockedIn = latestClockedIn.strftime('%Y-%m-%d %H:%M:%S') if latestClockedIn else ''
        attendance = Attendance.objects.filter(user_id=request.user.pk, status=False).order_by('-clock_time')
        latestClockedOut = attendance[0].clock_time if attendance else None
        latestClockedOut = latestClockedOut.strftime('%Y-%m-%d %H:%M:%S') if latestClockedOut else ''
        response['lastClockedIn'] = latestClockedIn
        response['latestClockedOut'] = latestClockedOut
    except AttributeError:
        response['error'] = ('Sorry, An error occurred while fetching the data.'
            'Please try again later')
    return JsonResponse(response)