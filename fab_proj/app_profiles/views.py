from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse


class LoginModel(LoginView):
    """Представление для авторизации"""
    template_name = 'profile/login.html'


class LogoutModel(LogoutView):
    """представление для выхода из системы (разрыва сессии)"""
    next_page = '/'
