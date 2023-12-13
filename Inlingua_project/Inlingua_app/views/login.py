from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def custom_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid login credentials.')

    return render(request, 'inlingua/login.html')
