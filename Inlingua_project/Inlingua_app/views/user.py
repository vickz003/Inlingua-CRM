from django.shortcuts import render, redirect
from django.contrib import messages
from Inlingua_app.models import User, TrainingStaff, StudentDetails, UserRoles, StudentDetails, TrainingBatches
import datetime
def user_page(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        user = User.objects.get(id=user_id)

        if user.is_staff:
            if user.is_superuser:
                if request.method == 'POST':
                    name = request.POST.get('name')
                    firstname = request.POST.get('fname')
                    lasttname = request.POST.get('lname')
                    Email = request.POST.get('gmail')
                    mobilenumber = request.POST.get('mobilenumber')
                    studentphoto = request.POST.get('studentphoto')
                    password1 = Email
                    Batchid = request.POST.get('Batchid')

                    Batchid = TrainingBatches.objects.get(ID = Batchid)
                    
                    newstudent = User.objects.create(
                        name = name,
                        first_name = firstname,
                        last_name = lasttname,
                        Mobile_Number = mobilenumber,
                        email = Email,
                        username = Email,
                        user_img = studentphoto,
                        created_by = user.name,
                        updated_by = user.name,
                        updated_date = datetime.datetime.now(),
                        role_id = UserRoles.objects.get(Name ='Student'),
                    )
                    newstudent.set_password(password1)
                    newstudent.save()
                    
                    lastuser = User.objects.last()
                    new_student_details = StudentDetails.objects.create(
                        StudentID = lastuser,
                        BatchID = Batchid
                    )
                    new_student_details.save()
                    messages.success(request, "Registration successful. You can now log in.")
                    return redirect('home')
                else:
                    Student_details = StudentDetails.objects.all()
                    Training_staff = TrainingStaff.objects.all()
                    batches = TrainingBatches.objects.all()
                    
                    context = {'User': user, 
                            'Training Staff': Training_staff, 
                            'Student_details':Student_details,
                            'batches':batches,
                            'Students':'active'}
                    return render(request, "inlingua/user.html",context)

            else:
                pass
        else:
            pass
    else:
        pass