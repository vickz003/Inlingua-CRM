from django.shortcuts import render, redirect
from django.contrib import messages
from Inlingua_app.models import User, Courses, Level, Languages, TrainingStaff, TrainerQualifications, TrainingBatches, StudentDetails

def home(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        user = User.objects.get(id=user_id)

        if user.is_staff:
            if user.is_superuser:
                return render(request, 'inlingua/index.html')
                # Handle superuser logic here (if needed)
            else:
                training_staff = TrainingStaff.objects.get(LoginId=user)
                trainer_qualifications = TrainerQualifications.objects.get(TrainerId=training_staff)
                training_batches = TrainingBatches.objects.filter(TrainerId=training_staff)
                return render(request, 'inlingua/index.html', {
                    'user': user,
                    'training_staff': training_staff,
                    'trainer_qualifications': trainer_qualifications,
                    'training_batches': training_batches,
                })
        # Stident details
        elif user.is_active:
            student_details = StudentDetails.objects.get(StudentID=user)
            training_batches = TrainingBatches.objects.get(ID = student_details.BatchID.ID)
            print(training_batches.ID)
            return render(request, 'inlingua/index.html', {
                'user': user,
                'student_details': student_details,
                'training_batches':training_batches,
            })
        else:
            messages.error(request, "Account is inactive.")
            return render(request, 'inlingua/index.html')
    else:
        messages.error(request, "Your account has been logged out. Please log in.")
        return redirect('login')
