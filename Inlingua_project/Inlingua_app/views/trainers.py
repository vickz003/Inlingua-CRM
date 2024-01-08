from django.shortcuts import render, redirect
from django.contrib import messages
from Inlingua_app.models import User, Languages, TrainerQualifications

def trainers_view(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        user = User.objects.get(id=user_id)

        if user.is_staff:
            if user.is_superuser:
                languages = Languages.objects.all()
                training_Staff = TrainerQualifications.objects.all()

                context = {'User': user, 'languages': languages, 'training_Staff':training_Staff}
                return render(request, "inlingua/trainers.html",context)
            else:
                pass
        else:
            pass
    else:
        pass



def trainer_view(request,id):
    if request.user.is_authenticated:
        user_id = request.user.id
        user = User.objects.get(id=user_id)

        if user.is_staff:
            if user.is_superuser:
                training_Staff = TrainerQualifications.objects.get(ID=id)

                context = {'User': user, 'training_Staff':training_Staff}
                return render(request, "inlingua/trainers.html",context)
            else:
                pass
        else:
            pass
    else:
        pass