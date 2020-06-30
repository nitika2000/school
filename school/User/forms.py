from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Userobject
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class BaseUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Userobject
        fields = ('email','name',)
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit = True):
        user = super(BaseUserCreationForm).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class BaseUserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Userobject
        fields = ('email', 'password','is_active', 'is_admin')

    def clean_password(self):
        return self.initial['password']

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = Userobject
        fields = ('email', 'password','name',)
    
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'placeholder': 'Email Address', 'class': 'col-md-12', 'required': 'required'}
    ))
    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Name', 'class': 'col-md-12 mb-3 mb-md-0', 'required': 'required'}
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', 'class':'col-md-12 mb-3 mb-md-0', 'required': 'required'}
    ))