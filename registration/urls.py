"""
URL configuration for registration project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include  # Include for app delegation
from Next_Click import views
from django_otp.views import LoginView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("admin/", admin.site.urls),         # Admin URL
    path('',views.SignupPage, name='signup'),
    path('login/',views.LoginPage, name ='login'),
    path('home/',views.HomePage, name ='home'),
    path("", include("Next_Click.urls")),    # Delegate all other URLs to the Next_Click app
    path('logout/',views.LogoutPage, name ='logout'),  
    path('otp/login/', LoginView.as_view(template_name='login.html'), name='otp_login'),
    path('forgot_password/', views.ForgotPassPage, name='forgot_password'),

    

]