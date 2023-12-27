from django.shortcuts import render, redirect
from django.contrib import messages
from Inlingua_app.models import (User, TrainingStaff, TrainerQualifications, TrainingBatches)

def batches(request,id):
    if request.user.is_authenticated:
        user_id = request.user.id
        user = User.objects.get(id=user_id)

        if user.is_staff == True:
            Training_staff = TrainingStaff.objects.get(LoginId = user_id)
            Trainer_qualifications = TrainerQualifications.objects.get(TrainerId = Training_staff.ID)
            Training_batches = TrainingBatches.objects.filter(TrainerId = Training_staff.ID)
            Training_Batch = TrainingBatches.objects.get(ID = id)
            return render(request, 'inlingua/index.html',
        {
        'user': user,
        'Training_staff':Training_staff,
        'Trainer_qualifications':Trainer_qualifications,
        'Training_batches':Training_batches,
        'Training_Batch':Training_Batch
        })
    else:
        messages.error(request, "Your account as been logout Please login...!")
        return redirect('login')
