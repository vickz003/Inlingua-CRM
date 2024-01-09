from django.shortcuts import render, redirect
from django.contrib import messages
from Inlingua_app.models import User, Level, Courses

def table_page(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        user = User.objects.get(id=user_id)

        if user.is_staff:
            if user.is_superuser:
                roles = Courses.objects.all()
                languages = Level.objects.all()
                context = {'User': user, 'roles': roles, 'languages':languages, 'courceandlevels':'active'}
                return render(request, "inlingua/courceandlevels.html",context)

            else:
                pass
        else:
            pass
    else:
        pass