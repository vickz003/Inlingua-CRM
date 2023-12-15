from django.shortcuts import render, redirect
from django.contrib import messages
from Inlingua_app.models import User, Courses, Level, Languages

def home(request):
    if not request.user.is_authenticated:
        return redirect('custom_login')

    user_id = request.user.id
    user = User.objects.get(id=user_id)
    cources = Courses.objects.get(Name = user.Course_details)
    level = Level.objects.get(Name = cources.LevelID)
    language = Languages.objects.get(Name = cources.LanguageID)

    
    context = {
        'user': user,
        'cources':cources,
        'level' : level,
        'language' : language,
        }
    return render(request, 'inlingua/index.html', context)


