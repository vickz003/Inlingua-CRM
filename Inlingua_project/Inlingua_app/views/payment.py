from django.shortcuts import render, redirect
from Inlingua_app.models import User, Payments, Courses, StudentDetails, PaymentMethod, PaymentTypes, PaymentStatus
import datetime


def payment_view(request,id):
    if request.user.is_authenticated:
        user_id = request.user.id
        user = User.objects.get(id=user_id)

        if user.is_staff:
            if user.is_superuser:
                paymentmethod = PaymentMethod.objects.all()
                paytypes = PaymentTypes.objects.all()
                paymentstatus = PaymentStatus.objects.all()
                history = Payments.objects.filter(StudentDetails=id)
                student_details = StudentDetails.objects.get(ID = id)
                total_amount = history.aggregate(Sum('Amount'))['Amount__sum'] or 0
                Course_cost = student_details.BatchID.Course_details.Cost
                pending_amountprint = student_details.BatchID.Course_details.Cost-total_amount
                                                                                     
                if request.method == 'POST':
                    PaymentTypeId = request.POST.get('PaymentTypeId')
                    PaymentMethodId   = request.POST.get('PaymentMethodId')
                    TransactionId  = request.POST.get('TransactionId')
                    Amount  = request.POST.get('Amount')
                    IsDiscountApplied  = request.POST.get('Discount')
                    DiscountedPayment  = request.POST.get('DiscountedPayment')
                    Description  = request.POST.get('Description')

                    if int(Amount) <= int(Course_cost) and int(pending_amountprint)>=int(Amount):
                        print("Correct")
                    else:
                        print("Rong")
                        return render(request,'inlingua/payment.html')
                                                   

                    if IsDiscountApplied == "on":
                        IsDiscountApplied = True
                    else:
                        IsDiscountApplied = False

                    try:
                        DiscountedPayment = int(DiscountedPayment)
                    except:
                        DiscountedPayment = 0

                    studentdetails = StudentDetails.objects.get(ID = id)
                    course = Courses.objects.get(ID = int(studentdetails.BatchID.Course_details.ID))
                    PaymentTypeId = PaymentTypes.objects.get(ID = int(PaymentTypeId))
                    PaymentMethodId = PaymentMethod.objects.get(ID = int(PaymentMethodId))

                    if int(Amount) + int(total_amount) == int(Course_cost):
                        Paymentstatus = PaymentStatus.objects.get(ID = 1)
                        
                    else:
                        Paymentstatus = PaymentStatus.objects.get(ID = 2)
                        

                    new_payment = Payments.objects.create(
                    StudentDetails = studentdetails,
                    PaymentTypeId = PaymentTypeId,
                    PaymentMethodId = PaymentMethodId ,
                    CourseId = course,
                    PaymentDate = datetime.datetime.now(),
                    TransactionId = TransactionId,
                    Amount = float(Amount),
                    PaymentStatus = Paymentstatus,
                    IsDiscountApplied = IsDiscountApplied,
                    DiscountedPayment = DiscountedPayment,
                    Description = Description,
                    CreatedBy = user.name,
                    CreatedDate = datetime.datetime.now(),
                    UpdatedBy = user.name,
                    UpdatedDate = datetime.datetime.now(),
                    )
                    new_payment.save()

            context ={
                'paymentmethod':paymentmethod,
                'paytypes':paytypes,
                'paymentstatus':paymentstatus,
            }
            return render(request,'inlingua/payment.html',context)

from django.db.models import Sum
def history_view(request,id):
    history = Payments.objects.filter(StudentDetails=id)
    student_details = StudentDetails.objects.get(ID = id)
    total_amount = history.aggregate(Sum('Amount'))['Amount__sum'] or 0
    pending_amountprint = student_details.BatchID.Course_details.Cost-total_amount
    try:
        last_history = history.last()
    except:
        pass
    context = {
        'history':history,
        'student_details':student_details,
        'last_history':last_history,
        'total_amount': total_amount,
        'pending_amountprint':pending_amountprint,
    }
    return render (request, 'inlingua/history.html', context)