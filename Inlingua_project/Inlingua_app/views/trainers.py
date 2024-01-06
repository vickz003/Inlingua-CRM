from django.shortcuts import render, redirect
from django.contrib import messages
from Inlingua_app.models import User, Languages, TrainingStaff

def trainers_view(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        user = User.objects.get(id=user_id)

        if user.is_staff:
            if user.is_superuser:
                languages = Languages.objects.all()
                training_Staff = TrainingStaff.objects.all()

                context = {'User': user, 'languages': languages, 'training_Staff':training_Staff}
                return render(request, "inlingua/trainers.html",context)
            else:
                pass
        else:
            pass
    else:
        pass