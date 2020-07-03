from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView, name='home'),
    path('about/', views.AboutUsView.as_view(), name='about'),
    path('signup/', views.SignUpView, name='signup'),
    path('login/', views.LoginView, name='login'),
    path('logout/',views.LogoutView, name='logout'),
]