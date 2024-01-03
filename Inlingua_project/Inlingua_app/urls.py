from django.urls import path
from Inlingua_app.views import login, home, register, logout, batchdetails, user
from django.contrib.auth import views as password_views


urlpatterns = [
    path('crm/login', login.custom_login, name="login"),
    path('logout', logout.custom_logout, name="logout"),
    path('crm/home', home.home, name="home"),
    path('crm/user', user.user_page, name="user"),
    path('crm/batch/<int:id>', batchdetails.batches, name="batches"),
    path('crm/user/register', register.register, name="register"),

    # Reset the password urls

    path('password_reset/',password_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',password_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',password_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',password_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]