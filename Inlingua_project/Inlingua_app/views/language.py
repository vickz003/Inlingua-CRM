from django.shortcuts import render, redirect
from django.contrib import messages
from Inlingua_app.models import User, TrainingStaff, TrainerQualifications, TrainingBatches, StudentDetails,UserRoles, Languages
from django.urls import reverse


def language_view(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        user = User.objects.get(id=user_id)

        if user.is_staff:
            if user.is_superuser:
                roles = UserRoles.objects.all()
                languages = Languages.objects.all()
                context = {'User': user, 'roles': roles, 'languages':languages,'showcontainer':'d-block'}
                return render(request, "inlingua/tables.html",context)

            else:
                pass
        else:
            pass
    else:
        pass


def add_language(request):
    if request.method == 'POST':
        name = request.POST.get('language')
        print(name)

        if name:
            if not Languages.objects.filter(Name=name).exists():
                print("Ok")
                language = Languages.objects.create(Name=name, CreatedBy=request.user.username, UpdatedBy=request.user.username)
                language.save()
                
                messages.success(request,"Language added successfully!")
                return redirect('tables')  

            else:
                messages.error(request,"This Language already exists.")
        else:
            messages.warning(request,"Please fill out all fields.")
    return redirect('tables') 

from Inlingua_app.forms import UserRolesForm
from django.http import Http404

def edit_view(request, id):
    if request.user.is_authenticated:
        user_id = request.user.id
        user = User.objects.get(id=user_id)

        if user.is_staff and user.is_superuser:
            if request.method == 'POST':
                role_name = request.POST.get('RoleName')
                description = request.POST.get('Roledesc')

                update_role = UserRoles.objects.get(ID=id)

                update_role.Name = role_name
                update_role.Description = description
                update_role.UpdatedBy = request.user.username
                update_role.UpdatedDate = datetime.datetime.now()

                update_role.save()

                return redirect('tables')  
            else:
                try:
                    get_data = UserRoles.objects.get(ID=id)
                except UserRoles.DoesNotExist:
                    raise Http404("Role does not exist")

                form = UserRolesForm(instance=get_data)

                roles = UserRoles.objects.all()
                languages = Languages.objects.all()
                context = {
                    'User': user,
                    'roles': roles,
                    'languages': languages,
                    'get_data': get_data,
                    'showdivcontainer': 'd-block',
                    'form': form,
                }
                return render(request, "inlingua/tables.html", context)
    else:
        pass  # Handle authentication failure if needed
