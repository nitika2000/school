from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import TemplateView
from .models import Userobject
from .forms import UserRegisterForm, LoginForm
# Create your views here.
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

class HomeView(TemplateView):
    template_name = 'home.html'

class AboutUsView(TemplateView):
    template_name = 'about.html'

def SignUpView(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            user = Userobject.object.create_user(
                email=email, password=password,name = name,
            )
            messages.success(
                request, "Registeration Successfull"
            )
            return redirect('User: home')
        else:
            if Userobject.object.is_email_registered(email = request.POST['email']):
                # messages.error(
                #     request, 'Given Email address is already registered'
                # )
                print("Given Email is registerede")
            else:
                print("Incorrect Details")
                # messages.error(request, 'Incorrect Details')
    else:
        form = UserRegisterForm()
    return render(request, 'signup.html', {'form': form})

def LoginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            obj = Userobject.object.filter(email=email).first()
            if obj is not None:
                obj = authenticate(email=email, password=password)
                if obj is not None:
                    login(request, obj)
                    return redirect('User : home')
                else:
                    print("Incorrect Username")
            else:
                print("Incorrect Username")
        else:
            print("Please enter valid data")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form':form})