from django.urls import path
from Next_Click import views
from django_otp.views import LoginView
from django.contrib import admin

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('Next_Click.urls')),  # Include app-level URLs
#     # Authentication URLs
#     path('', views.register, name='signup'),  # Registration page
#     path('login/', views.LoginPage, name='login'),  # Login page
#     path('logout/', views.LogoutPage, name='logout'),  # Logout page
#     # Home pag
#     path('home/', views.HomePage, name='home'),
# ]




urlpatterns = [
    path('',views.SignupPage, name='signup'),
    path('login/',views.LoginPage, name ='login'),
    path('home/',views.HomePage, name ='home'),
    path('logout/',views.LogoutPage, name ='logout'),
    path('otp/login/', LoginView.as_view(template_name='login.html'), name='otp_login'),
    path('forgot_password/', views.ForgotPassPage, name='forgot_password'),
    
]
