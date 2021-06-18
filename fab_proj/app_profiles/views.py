from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse


class LoginModel(LoginView):
    template_name = 'profile/login.html'


class LogoutModel(LogoutView):
    next_page = '/'
