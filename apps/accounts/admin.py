from django.contrib import admin
from .models import User, Role, Permission, UserRole, RolePermission

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email')

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'module')
    list_filter = ('module',)

admin.site.register(UserRole)
admin.site.register(RolePermission)
