from django.contrib import admin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

# Register your models here.
from django import forms
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Userobject
from .forms import BaseUserChangeForm, BaseUserCreationForm

class UserAdmin(BaseUserAdmin):
    form = BaseUserChangeForm
    add_form = BaseUserCreationForm

    list_display = ('email', 'name', 'is_admin',)
    list_filter = ('is_admin',)

    fieldsets = (
        (None, {'fields' : ('email', 'password',)}),
        ('Personal info',{'fields': ('name',)}),
        ('Permissions', {'fields': ('is_admin','is_active')}),
    )

    add_fieldsets = (
        (None,{
            'classes': ('wide',),
            'fields' : ('email', 'password1', 'password2',),
        }

        ),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(Userobject, UserAdmin)
# admin.site.unregister(Group)