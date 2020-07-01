from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import TemplateView
from .models import Userobject
from .forms import UserRegisterForm
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
            return redirect('accounts: home')
        else:
            if Userobject.object.is_email_registered(email = request.POST['email']):
                # messages.error(
                #     request, 'Given Email address is already registered'
                # )
                print("Given Email")
            else:
                print("Incorrect Details")
                # messages.error(request, 'Incorrect Details')
    else:
        form = UserRegisterForm()
    return render(request, 'signup.html', {'form': form})