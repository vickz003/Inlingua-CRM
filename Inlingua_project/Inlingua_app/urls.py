from django.urls import path
from Inlingua_app.views import login,home,register

urlpatterns = [
    path('crm/login',login.custom_login,name="login"),
    path('crm/home',home.home,name="home"),
    path('crm/user/register',register.register,name="register"),
]
