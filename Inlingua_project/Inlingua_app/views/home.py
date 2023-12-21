from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import Http404
from Inlingua_app.models import User, Courses, Level, Languages

def home(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        user = User.objects.get(id=user_id)

        try:
            cources = Courses.objects.get(Name=user.Course_details)
        except Courses.DoesNotExist:
            if user.is_staff == True:
                return render(request, 'inlingua/index.html', 
            {
            'user': user,})
            else:
                messages.error(request, "Course does not exist")
                return render(request, 'inlingua/error_template.html')

        level = Level.objects.get(Name=cources.LevelID)
        language = Languages.objects.get(Name=cources.LanguageID)
        return render(request, 'inlingua/index.html', {
            'user': user,
            'cources': cources,
            'level': level,
            'language': language,
        })
    else:
        messages.error(request, "Your account as been logout Please login...!")
        return redirect('login')
