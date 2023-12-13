from django.shortcuts import render, redirect
from django.contrib import messages
from Inlingua_app.models import User, UserRoles

def register(request):
    if request.method == "POST":
        roles = request.POST.get('roles')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        created_by = request.user.username 

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('home') 

        try:
            role_object = UserRoles.objects.get(Name=roles)

            user = User.objects.create(
                username=username,
                role_id=role_object,
                created_by=created_by
            )

            user.set_password(password1)
            
            user.save()

            messages.success(request, "Registration successful. You can now log in.")
            return redirect('login')
        except UserRoles.DoesNotExist:
            messages.error(request, "Invalid role selected.")
        except Exception as e:
            messages.error(request, f"Registration failed: {e}")

    return redirect('home') 
