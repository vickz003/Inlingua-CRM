from django.shortcuts import render, redirect
from django.contrib import messages
from Inlingua_app.models import User, Languages, TrainerQualifications

def language_view(request,name):
    if request.user.is_authenticated:
        user_id = request.user.id
        user = User.objects.get(id=user_id)

        if user.is_staff:
            if user.is_superuser:
                languages = Languages.objects.get(Name = name)
                Trainers = TrainerQualifications.objects.filter(LanguageID = languages.ID)

                context = {'User': user,'languages':languages, 'Trainers':Trainers}
                return render(request, "inlingua/language_page.html",context)
            else:
                pass
        else:
            pass
    else:
        pass