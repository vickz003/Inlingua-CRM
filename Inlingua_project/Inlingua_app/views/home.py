from django.shortcuts import render, redirect
from django.contrib import messages
from Inlingua_app.models import User

def home(request):
    if not request.user.is_authenticated:
        return redirect('custom_login')

    user_id = request.user.id
    user_details = User.objects.get(id=user_id)
    return render(request, 'inlingua/index.html', {'user_details': user_details})


