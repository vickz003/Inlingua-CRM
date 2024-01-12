from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib import messages
from django.urls import reverse
from Inlingua_app.models import User, Level, Courses, TrainingBatches,TrainingStaff, Languages, Courses

def table_page(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        user = User.objects.get(id=user_id)

        if user.is_staff:
            if user.is_superuser:
                All_batches = TrainingBatches.objects.all()
                All_courses = Courses.objects.all()
                All_level = Level.objects.all()
                All_languages = Languages.objects.all()
                training_staff = TrainingStaff.objects.all()
                context = {'courceandlevels':'active',
                           'User': user, 
                           'All_batches': All_batches, 
                           'All_courses':All_courses,
                           'All_level':All_level,
                           'All_languages':All_languages,
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
                if request.method == 'POST':
                    batchname = request.POST['batchname']
                    Courses_Details = request.POST['Courses_Details']
                    Trainer = request.POST['Trainer']
                    gmeeturl = request.POST['gmeeturl']
                    satrdate = request.POST['satrdate']
                    EndDate = request.POST['EndDate']
                    classduraition = request.POST['classduraition']
                    start_time = request.POST['start_time']
                    end_time = request.POST['end_time']
                    end_time = request.POST['end_time']

                    Courses_Details = Courses.objects.get(ID = int(Courses_Details))
                    Trainer = TrainingStaff.objects.get(ID = int(Trainer))

                    new_batch = TrainingBatches.objects.create(
                        Name = batchname,
                        Course_details = Courses_Details,
                        TrainerId = Trainer,
                        MeetingURL = gmeeturl,
                        StartDate = satrdate,
                        EndDate = EndDate,
                        Duration = classduraition,
                        StartTime = start_time,
                        EndTime = end_time,
                        IsActive = True,
                        CreatedBy=user.name,
                        CreatedDate= datetime.datetime.now(),
                        UpdatedBy=user.name,
                        UpdatedDate= datetime.datetime.now(),
                        )
                    new_batch.save()
                    return redirect('courceandlevels_table')
                else:
                    pass
            else:
                print("Yes iam 2")
        else:
            print("Yes ima 3")
    else:
        print("Yes iam 4")


def edit_batchs(request,id):
    if request.user.is_authenticated:
        user_id = request.user.id
        user = User.objects.get(id=user_id)

        if user.is_staff:
            if request.user.is_superuser:
                if request.method == 'POST':
                    pass
                else:
                    batch_info = TrainingBatches.objects.get(ID=id)
                    All_courses = Courses.objects.all()
                    training_staff = TrainingStaff.objects.all()

                    context = {'id': id, 'BatchInfo': batch_info,'All_courses':All_courses, 'training_staff':training_staff}
                    context['url_with_id'] = reverse('edit_batchs', kwargs={'id': id})
                    return render(request, "inlingua/courceandlevels.html", context)
            else:
                return redirect('login_page')
        else:
            pass

def add_course(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        user = User.objects.get(id=user_id)

        if user.is_staff:
            if user.is_superuser:
                if request.method == 'POST':
                    course_name = request.POST['coursename']
                    level_details = request.POST['levelid']
                    language_details = request.POST['languageid']
                    course_duration = request.POST['duration']
                    cost = request.POST['cast']
                    start_date = request.POST['satrdate']
                    end_date = request.POST['EndDate']
                    start_time = request.POST['start_time']
                    end_time = request.POST['end_time']
                    course_metirials = request.POST['coursemetrials']
                    course_status = request.POST['coursestatus']
                    duscription = request.POST['Duscription']
                    
                    language_details = Languages.objects.get(ID=int(language_details))
                    level_details = Level.objects.get(ID=int(level_details))
                    new_courses = Courses.objects.create(
                        Name = course_name,
                        Description = duscription,
                        Duration = course_duration,
                        LanguageID =language_details,
                        StartDate = start_date,
                        EndtDate = end_date,
                        StartTime = start_time,
                        EndTime = end_time,
                        LevelID = level_details,
                        Cost = cost,
                        Course_metirials = course_metirials,
                        Course_status = course_status,
                        CreatedBy=user.name,
                        CreatedDate= datetime.datetime.now(),
                        UpdatedBy=user.name,
                        UpdatedDate= datetime.datetime.now(),
                        )
                    new_courses.save()
                    return redirect('courceandlevels_table')
                else:
                    pass
            else:
                print("Yes iam 2")
        else:
            print("Yes ima 3")
    else:
        print("Yes iam 4")
                    

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
                    