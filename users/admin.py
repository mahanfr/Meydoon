from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class UserConfig(UserAdmin):
    model = User
    search_fields = ('email','user_name','phone_number')
    list_filter = ('is_active','is_staff','is_superuser')
    ordering = ('-created_at',)
    list_display = ('email','user_name','phone_number','is_active','is_staff')

    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'phone_number',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'phone_number', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )

# Register your models here.
admin.site.register(User,UserConfig)