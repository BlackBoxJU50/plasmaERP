from django.urls import path
from . import views, api_views

app_name= 'hrm'

urlpatterns = [
    path('employees/', views.employee_list_view, name='employee_list'),
    path('employees/add/', views.employee_create_view, name='employee_add'),
    path('employees/<int:pk>/edit/', views.employee_edit_view, name='employee_edit'),
    path('employees/<int:pk>/delete/', views.employee_delete_view, name='employee_delete'),

    path('departments/', views.department_list_view, name='department_list'),
    path('departments/add/', views.department_create_view, name='department_add'),

    path('designations/', views.designation_list_view, name='designation_list'),
    path('designations/add/', views.designation_create_view, name='designation_add'),

    path('leaves/', views.leave_list_view, name='leave_list'),
    path('leaves/add/', views.leave_create_view, name='leave_add'),

    path('payroll/', views.payroll_list_view, name='payroll_list'),
    path('payroll/add/', views.payroll_create_view, name='payroll_add'),

    path('attendance/', views.attendance_list_view, name='attendance_list'),
    path('attendance/add/', views.attendance_create_view, name='attendance_add'),
    path('attendance/report/', views.attendance_report_view, name='attendance_report'),
    path('attendance/report/pdf/', views.attendance_pdf_view, name='attendance_pdf'),
    path('attendance/report/excel/', views.attendance_excel_view, name='attendance_excel'),
    
    # Webhook API
    path('api/attendance/webhook/', api_views.google_sheet_webhook, name='attendance_webhook'),
]