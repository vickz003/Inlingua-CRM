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
                                                                                     
                if request.method == 'POST':
                    PaymentTypeId = request.POST.get('PaymentTypeId')
                    PaymentMethodId   = request.POST.get('PaymentMethodId')
                    TransactionId  = request.POST.get('TransactionId')
                    Amount  = request.POST.get('Amount')
                    Paymentstatus  = request.POST.get('PaymentStatus')
                    IsDiscountApplied  = request.POST.get('Discount')
                    DiscountedPayment  = request.POST.get('DiscountedPayment')
                    Description  = request.POST.get('Description')

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
                    Paymentstatus = PaymentStatus.objects.get(ID = int(Paymentstatus))

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
        
def history_view(request,id):
    return render (request, 'inlingua/history.html',{'id':id})