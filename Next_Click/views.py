from django.shortcuts import render,HttpResponse,redirect
import os
from pathlib import Path
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.core.exceptions import ValidationError
import re

from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings


@login_required(login_url='login')

# Create your views here.
def HomePage(request):
    template_path = Path('C:/Users/Lavish/CS_IA/Registration System/registration/Templates/home.html')
    return render(request, template_path)

def SignupPage(request):
    if request.method == 'POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        my_user=User.objects.create_user(uname,email,pass1)
        my_user.save()
        return redirect('login')

    return render (request, 'register.html')


def LoginPage(request):
    error = None
    if request.method == 'POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        if not username or not pass1:
            error = "Both Fields are Required"
        else:
            user=authenticate(request,username=username,password = pass1)
            if user is not None: #change this to a better and more imporved version, check username and password individually 
                login(request,user)
                return redirect("home")
            else:
                return render(request, "login.html", {'error': 'Invalid Username or Password'})


    return render (request, 'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')


# ********* Password **********
def validate_special_characters(password):
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        raise ValidationError("Password must contain at least one special character.")
    

# AUTH_PASSWORD_VALIDATORS += [
#     {
#         'NAME': 'path.to.validate_special_characters',
#     },
# ]


def ForgotPassPage(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            associated_users = User.objects.filter(email=email)
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "emails/password_reset_email.txt"
                    context = {
                        "email": user.email,
                        "domain": request.get_host(),
                        "site_name": "Your Site Name",
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        "token": default_token_generator.make_token(user),
                        "protocol": "http" if not request.is_secure() else "https",
                    }
                    email_text = render_to_string(email_template_name, context)
                    try:
                        send_mail(subject, email_text, settings.DEFAULT_FROM_EMAIL, [user.email])
                    except BadHeaderError:
                        return HttpResponse("Invalid header found.")
                    return redirect('password_reset_done')  # this should be a view or template
            else:
                return render(request, 'forgot_password.html', {'form': form, 'error': 'No user with this email.'})
    else:
        form = PasswordResetForm()

    return render(request, 'forgot_password.html', {'form': form})