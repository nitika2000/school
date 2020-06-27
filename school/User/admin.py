from django.contrib import admin

# Register your models here.
from django import forms
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Userobject
from .forms import BaseUserChangeForm, BaseUserCreationForm

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Userobject
        fields = ('email',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserAdmin(BaseUserAdmin):
    form = BaseUserChangeForm
    add_form = BaseUserCreationForm

    list_display = ('email', 'is_admin')
    list_filter = ('is_admin')

    fieldsets = (
        (None, {'fields' : ('email', 'password')}),
        ('Permissions', {'fields': ('is_admin','is_active')}),
    )

    add_fieldsets = (
        (None,{
            'classes': ('wide',),
            'fields' : ('email', 'password1', 'password2'),
        }

        ),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(Userobject, UserAdmin)
admin.site.unregister(Group)