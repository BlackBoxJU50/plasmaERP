from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name= 'hrm'

urlpatterns = [
    path('employees/', views.employee_list_view, name='employee_list'),
    path('employees/add/', views.employee_create_view, name='employee_add'),
      
]   