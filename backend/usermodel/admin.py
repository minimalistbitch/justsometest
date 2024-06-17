# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from requests import request

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'is_staff', 'is_superuser']
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                    'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'is_staff', 'is_superuser'),
        }),
    )

    def save_model(self, request, obj, form, change):
        if 'is_staff' in form.cleaned_data and form.cleaned_data['is_staff']:
            obj.is_staff = True
        if 'is_superuser' in form.cleaned_data and form.cleaned_data['is_superuser']:
            obj.is_superuser = True
        obj.save()

    def create_staff_user(self, request, queryset):
        for user in queryset:
            user.is_staff = True
            user.save()

    create_staff_user.short_description = "Mark selected users as staff"

admin.site.register(CustomUser, CustomUserAdmin)
