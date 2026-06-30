from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import date

@login_required(login_url='login')
def dashboard_view(request):
    from apps.hrm.models import Employee, Attendance, Department, LeaveRequest

    today = date.today()

    total_employees  = Employee.objects.filter(status=True).count()
    total_departments = Department.objects.count()
    today_present    = Attendance.objects.filter(date=today, status='Present').count()
    today_late       = Attendance.objects.filter(date=today, status='Late').count()
    today_absent     = Attendance.objects.filter(date=today, status='Absent').count()
    pending_leaves   = LeaveRequest.objects.filter(status='Pending').count()

    # Recent attendance (last 7 records)
    recent_attendance = (
        Attendance.objects
        .filter(date=today)
        .select_related('employee', 'employee__department')
        .order_by('-created_at')[:10]
    )

    context = {
        'total_employees':  total_employees,
        'total_departments': total_departments,
        'today_present':    today_present,
        'today_late':       today_late,
        'today_absent':     today_absent,
        'pending_leaves':   pending_leaves,
        'recent_attendance': recent_attendance,
        'today': today,
    }
    return render(request, 'core/dashboard.html', context)
