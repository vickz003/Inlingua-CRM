import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from Inlingua_app.models import (User, Languages, TrainerQualifications, TrainingBatches, 
                                 StudentDetails, UserRoles,TrainingStaff, Level)

def trainers_view(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        
        if user.is_staff:
            if user.is_superuser:
                if request.method == 'POST':
                    name = request.POST.get('trainername')
                    firstname = request.POST.get('fname')
                    lasttname = request.POST.get('lname')
                    Email = request.POST.get('gmail')
                    mobilenumber = request.POST.get('mobilenumber')
                    studentphoto = request.POST.get('studentphoto')
                    password1 = Email
                    address = request.POST.get('Address')

                    certificateNumber = request.POST.get('studentphoto')
                    certifyingAuthority = request.POST.get('certifyingAuthority')
                    certificateValidTill = request.POST.get('certificateValidTill')
                    Language = request.POST.get('Language')
                    level = request.POST.get('level')

                    
                    newtrainer = User.objects.create(
                        name = name,
                        first_name = firstname,
                        last_name = lasttname,
                        Mobile_Number = mobilenumber,
                        email = Email,
                        username = Email,
                        user_img = studentphoto,
                        Address = address,
                        created_by = user.name,
                        updated_by = user.name,
                        is_staff = True,
                        updated_date = datetime.datetime.now(),
                        role_id = UserRoles.objects.get(Name ='Trainer'),
                    )
                    newtrainer.set_password(password1)
                    newtrainer.save()
                    
                    lastuser = User.objects.last()
                    new_trainer_details = TrainingStaff.objects.create(
                        Name = name,
                        EmailID = Email,
                        LoginId = lastuser,
                        IsActive = True,
                        CreatedBy = user.name,
                        CreatedDate = datetime.datetime.now(),
                        UpdatedBy = user.name,
                        UpdatedDate = datetime.datetime.now(),
                    )
                    new_trainer_details.save()

                    Language = Languages.objects.get(ID = int(Language))
                    level = Level.objects.get(ID = int(level))
                    lastuser = TrainingStaff.objects.last()
                    
                    new_trainer_qualification = TrainerQualifications.objects.create(
                        LanguageID = Language,
                        LevelId = level,
                        CertificateNumber = certificateNumber,
                        CertifyingAuthority = certifyingAuthority,
                        CertificateValidTill = certificateValidTill,
                        TrainerId = lastuser,
                        CreatedBy = user.name,
                        CreatedDate = datetime.datetime.now(),
                        UpdatedBy = user.name,
                        UpdatedDate = datetime.datetime.now(),
                    )
                    new_trainer_qualification.save()
                    
                    messages.success(request, "Registration successful. You can now log in.")
                    return redirect('home')
                else:
                    languages = Languages.objects.all()
                    levels = Level.objects.all()
                    training_Staff = TrainerQualifications.objects.all()
                    context = {'User': user, 
                               'languages': languages, 
                               'training_Staff':training_Staff,
                               'levels':levels,
                               'Trainers':'active'}
                    return render(request, "inlingua/trainers.html",context)
                     



def trainer_view(request,id):
    if request.user.is_authenticated:
        user_id = request.user.id
        user = User.objects.get(id=user_id)

        if user.is_staff:
            if user.is_superuser:
                training_Staff = TrainerQualifications.objects.get(ID=id)
                training_batches = TrainingBatches.objects.filter(TrainerId = training_Staff.TrainerId.ID)
                Student_details = StudentDetails.objects.all()
                
                context = {'User': user,
                           'Trainers':'active',
                           'training_Staff':training_Staff,
                           'training_batches':training_batches,
                           'Student_details':Student_details,
                           }
                return render(request, "inlingua/trainers.html",context)
            else:
                pass
        else:
            pass
    else:
        pass