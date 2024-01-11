from django.shortcuts import render, redirect
from django.contrib import messages
from Inlingua_app.models import User, Level, Courses, TrainingBatches,TrainingStaff

def table_page(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        user = User.objects.get(id=user_id)

        if user.is_staff:
            if user.is_superuser:
                All_batches = TrainingBatches.objects.all()
                All_courses = Courses.objects.all()
                All_level = Level.objects.all()
                training_staff = TrainingStaff.objects.all()
                context = {'courceandlevels':'active',
                           'User': user, 
                           'All_batches': All_batches, 
                           'All_courses':All_courses,
                           'All_level':All_level,
                           'training_staff':training_staff,
                           }
                return render(request, "inlingua/courceandlevels.html",context)

            else:
                pass
        else:
            pass
    else:
        pass

import datetime

def add_batchs(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        user = User.objects.get(id=user_id)

        if user.is_staff:
            if user.is_superuser:
                pass

def add_course(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        user = User.objects.get(id=user_id)

        if user.is_staff:
            if user.is_superuser:
                pass

def add_level(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        user = User.objects.get(id=user_id)

        if user.is_staff:
            if user.is_superuser:
                if request.method == 'POST':
                    level_name = request.POST['levelname']
                    level_code = request.POST['levelcode']
                    # Creadedby, creaded date, updateby, updatyedby
                    new_level = Level.objects.create(
                        Name=level_name, 
                        Code=level_code,
                        CreatedBy=user.name,
                        CreatedDate= datetime.datetime.now(),
                        UpdatedBy=user.name,
                        UpdatedDate= datetime.datetime.now(),
                        )
                    new_level.save()
                    return redirect('courceandlevels_table')
                else:
                    pass
            else:
                print("Yes iam 2")
        else:
            print("Yes ima 3")
    else:
        print("Yes iam 4")
                    