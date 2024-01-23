from django.urls import path

from Inlingua_app.views import (login, home, register, logout, batchdetails, user, tables, language as lng, roles, trainers, language_page, courceandlevels,payment)

from Inlingua_app.views import (login, home, register, logout, batchdetails, user, tables, language as lng, roles, trainers, language_page, courceandlevels)

from django.contrib.auth import views as password_views



urlpatterns = [
    path('crm/login', login.custom_login, name="login"),
    path('logout', logout.custom_logout, name="logout"),
    path('crm/home', home.home, name="home"),
    path('crm/students', user.user_page, name="students"),

    path('crm/students/payment/<int:id>', payment.payment_view, name='payment'),
    path('crm/students/payment/history/<int:id>', payment.history_view, name='history'),

    path('crm/trainers', trainers.trainers_view, name="trainers"),
    path('crm/trainers/<int:id>', trainers.trainer_view, name="trainer"),
    path('crm/tables', tables.table_page, name="tables"),
    path('crm/tables/addlanguage', lng.language_view, name="language"),
    path('crm/tables/addlanguage/add', lng.add_language, name="add_language"),
    path('crm/tables/language/<int:id>', lng.edit_lang, name="edit_lang"),
    path('crm/tables/language/delete/<int:id>', lng.delete_langu, name="delete_langu"),

    # batch courece and Levels urls-------------------------------------------------

    path('crm/courceandlevels_table', courceandlevels.table_page, name="courceandlevels_table"),

    # path('crm/tables/addlanguage', lng.language_view, name="language"),
    # path('crm/tables/addlanguage/add', lng.add_language, name="add_language"),
    # path('crm/tables/language/<int:id>', lng.edit_lang, name="edit_lang"),
    # path('crm/tables/language/delete/<int:id>', lng.delete_langu, name="delete_langu"),

    path('crm/courceandlevels_table/batchs/<int:id>', courceandlevels.edit_batchs, name="edit_batchs"),
    path('crm/courceandlevels_table/cources/<int:id>', courceandlevels.edit_cources, name="edit_cources"),
    path('crm/courceandlevels_table/level/<int:id>', courceandlevels.edit_level, name="edit_level"),


    path('crm/courceandlevels_table/add_level', courceandlevels.add_level, name="add_level"),
    path('crm/courceandlevels_table/add_course', courceandlevels.add_course, name="add_course"),
    path('crm/courceandlevels_table/add_batchs', courceandlevels.add_batchs, name="add_batchs"),
    


    path('crm/tables/addrole',roles.role_view, name="roles"),
    path('crm/tables/addrole/add',roles.add_role, name="add_roles"),
    path('crm/tables/roles/<int:id>', roles.edit_view, name="etit_view"),
    path('crm/tables/roles/delete/<int:id>', roles.delete_role, name="delete_role"),
    path('crm/language/<str:name>', language_page.language_view, name="language_view"),
    path('crm/batch/<int:id>', batchdetails.batches, name="batches"),
    path('crm/user/register', register.register, name="register"),

    # Reset the password urls

    path('password_reset/',password_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',password_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',password_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',password_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]
