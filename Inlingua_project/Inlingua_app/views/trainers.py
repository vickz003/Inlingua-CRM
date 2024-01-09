from django.shortcuts import render, redirect
from django.contrib import messages
from Inlingua_app.models import User, Languages, TrainerQualifications, TrainingBatches, StudentDetails

def trainers_view(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        Trainers = 'active'

        if user.is_staff:
            if user.is_superuser:
                languages = Languages.objects.all()
                training_Staff = TrainerQualifications.objects.all()
                Trainers = 'active'
                context = {'User': user, 'languages': languages, 'training_Staff':training_Staff,'Trainers':Trainers}
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