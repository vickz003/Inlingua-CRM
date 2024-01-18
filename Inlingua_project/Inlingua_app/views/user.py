from django.shortcuts import render, redirect
from django.contrib import messages
from Inlingua_app.models import User, TrainingStaff, TrainerQualifications, TrainingBatches, StudentDetails

def user_page(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        user = User.objects.get(id=user_id)

        if user.is_staff:
            if user.is_superuser:
                
                Student_details = StudentDetails.objects.all()
                Training_staff = TrainingStaff.objects.all()
                
                context = {'User': user, 
                           'Training Staff': Training_staff, 
                           'Student_details':Student_details, 
                           'Students':'active'}
                return render(request, "inlingua/user.html",context)

            else:
                pass
        else:
            pass
    else:
        pass