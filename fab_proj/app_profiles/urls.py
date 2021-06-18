from django.urls import path
from app_profiles.views import LoginModel, LogoutModel

urlpatterns = [
    path('login/', LoginModel.as_view(), name='login'),
    path('logout/', LogoutModel.as_view(), name='logout'),
]
