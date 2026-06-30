import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Employee, Attendance
from datetime import datetime, date

# Security token (Use environment variables in production)
WEBHOOK_SECRET = "plasma_secure_webhook_123"

@csrf_exempt
@require_POST
def google_sheet_webhook(request):
    """
    Receives JSON payload from Google Apps Script to log fingerprint attendance.
    """
    try:
        data = json.loads(request.body)
        
        if data.get('secret') != WEBHOOK_SECRET:
            return JsonResponse({'error': 'Unauthorized'}, status=401)
            
        employee_code = data.get('employee_code')
        record_date_str = data.get('date')
        
        if not employee_code or not record_date_str:
            return JsonResponse({'error': 'Missing employee_code or date'}, status=400)
            
        try:
            employee = Employee.objects.get(employee_code=employee_code)
        except Employee.DoesNotExist:
            return JsonResponse({'error': f'Employee with code {employee_code} not found'}, status=404)
            
        record_date = datetime.strptime(record_date_str, '%Y-%m-%d').date()
        
        check_in = None
        check_out = None
        working_hours = None
        
        if data.get('check_in'):
            check_in = datetime.strptime(data.get('check_in'), '%H:%M').time()
            
        if data.get('check_out'):
            check_out = datetime.strptime(data.get('check_out'), '%H:%M').time()
            
        if check_in and check_out:
            # Calculate working hours
            td_in = datetime.combine(date.min, check_in) - datetime.min
            td_out = datetime.combine(date.min, check_out) - datetime.min
            duration = td_out - td_in
            working_hours = round(duration.total_seconds() / 3600, 2)
            
        status = data.get('status', 'Present')
        
        attendance, created = Attendance.objects.update_or_create(
            employee=employee,
            date=record_date,
            defaults={
                'check_in': check_in,
                'check_out': check_out,
                'working_hours': working_hours,
                'status': status
            }
        )
        
        return JsonResponse({
            'success': True, 
            'message': f'Attendance {"created" if created else "updated"} for {employee_code}',
            'working_hours': working_hours
        })
        
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
