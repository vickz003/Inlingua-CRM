# models.py

from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import FileExtensionValidator

class CustomUserManager(BaseUserManager):
    def _create_user(self, email = None, password=None, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email = None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)

class Languages(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    IsActive = models.BooleanField(default=True)
    CreatedDate = models.DateTimeField(default=timezone.now)
    CreatedBy = models.CharField(max_length=255)
    UpdatedDate = models.DateTimeField(default=timezone.now)
    UpdatedBy = models.CharField(max_length=255)

    def __str__(self):
        return self.Name

class Level(models.Model):
    ID = models.AutoField(primary_key=True)
    Code = models.CharField(max_length=2)
    Name = models.CharField(max_length=255)
    CreatedBy = models.CharField(max_length=255)
    CreatedDate = models.DateTimeField(default=timezone.now)
    UpdatedBy = models.CharField(max_length=255)
    UpdatedDate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.Name

class Courses(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=255)
    Duration = models.IntegerField()
    LanguageID = models.ForeignKey(Languages, on_delete=models.CASCADE)
    StartDate = models.DateField(null=True, blank=True)
    EndtDate = models.DateField(null=True, blank=True)
    StartTime = models.TimeField(null=False, blank=False)
    EndTime = models.TimeField(null=False, blank=False)
    LevelID = models.ForeignKey(Level, on_delete=models.CASCADE)
    Cost = models.IntegerField()
    Course_metirials = models.FileField(
        upload_to='static/uploads/Stady_metirials',
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(allowed_extensions=['pdf', 'xls', 'xlsx',])
        ]
    )
    Course_status = models.IntegerField(default=0)
    CreatedDate = models.DateTimeField(default=timezone.now)
    CreatedBy = models.CharField(max_length=255)
    UpdatedDate = models.DateTimeField(default=timezone.now)
    UpdatedBy = models.CharField(max_length=255)
    
    def __str__(self):
        return self.Name
    
class PaymentStatus(models.Model):
    ID = models.AutoField(primary_key=True)
    StatusName = models.CharField(max_length=255)
    CreatedDate = models.DateTimeField(default=timezone.now)
    CreatedBy = models.CharField(max_length=255)
    UpdatedDate = models.DateTimeField(default=timezone.now)
    UpdatedBy = models.CharField(max_length=255)

    def __str__(self):
        return self.StatusName


class PaymentTypes(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=20)
    Description = models.CharField(max_length=255)
    CreatedBy = models.CharField(max_length=255)
    CreatedDate = models.DateTimeField(default=timezone.now)
    UpdatedBy = models.CharField(max_length=255)
    UpdatedDate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.Name

class PaymentMethod(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=20)
    CreatedBy = models.CharField(max_length=255)
    CreatedDate = models.DateTimeField(default=timezone.now)
    UpdatedBy = models.CharField(max_length=255)
    UpdatedDate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.Name
    
class Payments(models.Model):
    ID = models.AutoField(primary_key=True)
    StudentDetails = models.ForeignKey('StudentDetails', on_delete=models.CASCADE, null=True, blank=True)
    PaymentTypeId = models.ForeignKey(PaymentTypes, on_delete=models.CASCADE)
    PaymentMethodId = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE,null=True, blank=True)
    CourseId = models.ForeignKey(Courses, on_delete=models.CASCADE)
    PaymentDate = models.DateTimeField(default=timezone.now)
    TransactionId = models.CharField(max_length=100)
    Amount = models.DecimalField(max_digits=8, decimal_places=2,null=True, blank=True)
    PaymentStatus = models.ForeignKey(PaymentStatus, on_delete=models.CASCADE,null=True, blank=True)
    IsDiscountApplied = models.BooleanField()
    DiscountedPayment = models.IntegerField(default=0)
    Description = models.TextField(null=True, blank=True)
    CreatedBy = models.CharField(max_length=255)
    CreatedDate = models.DateTimeField(default=timezone.now)
    UpdatedBy = models.CharField(max_length=255, null=True, blank=True)
    UpdatedDate = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.StudentDetails)

class UserRoles(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=255)
    IsActive = models.BooleanField()
    CreatedBy = models.CharField(max_length=255)
    CreatedDate = models.DateTimeField(default=timezone.now)
    UpdatedBy = models.CharField(max_length=255)
    UpdatedDate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.Name

class User(AbstractUser):
    name = models.CharField(max_length=225, blank=True, null=True)
    Mobile_Number = models.IntegerField(null=True, blank=True)
    user_img = models.ImageField(upload_to='static/img/uploads/Profiles', blank=True, null=True)
    Address = models.CharField(max_length=400, null=True, blank=True)
    created_by = models.CharField(max_length=255)
    updated_by = models.CharField(max_length=255, null=True, blank=True)
    updated_date = models.DateTimeField(null=True, blank=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    role_id = models.ForeignKey(UserRoles, on_delete=models.CASCADE, null=True, blank=True)
    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        return super().save(*args, **kwargs)

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name or self.email.split('@')[0]

class ManagementStaff(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200)
    EmailID = models.CharField(max_length=200)
    IsSuperAdmin = models.BooleanField()
    IsAdmin = models.BooleanField()
    LoginId = models.ForeignKey(User, on_delete=models.CASCADE)
    IsActive = models.BooleanField()
    CreatedBy = models.CharField(max_length=255)
    CreatedDate = models.DateTimeField(default=timezone.now)
    UpdatedBy = models.CharField(max_length=255, null=True, blank=True)
    UpdatedDate = models.DateTimeField(null=True, blank=True)

class TrainingStaff(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200)
    EmailID = models.CharField(max_length=200)
    LoginId = models.ForeignKey(User, on_delete=models.CASCADE)
    IsActive = models.BooleanField()
    CreatedBy = models.CharField(max_length=255)
    CreatedDate = models.DateTimeField(default=timezone.now)
    UpdatedBy = models.CharField(max_length=255, null=True, blank=True)
    UpdatedDate = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.Name

class TrainerQualifications(models.Model):
    ID = models.AutoField(primary_key=True)
    LanguageID = models.ForeignKey(Languages, on_delete=models.CASCADE)
    LevelId = models.ForeignKey(Level, on_delete=models.CASCADE)
    CertificateNumber = models.CharField(max_length=255)
    CertifyingAuthority = models.CharField(max_length=255)
    CertificateValidTill = models.DateTimeField()
    CreatedBy = models.CharField(max_length=255)
    CreatedDate = models.DateTimeField(default=timezone.now)
    UpdatedBy = models.CharField(max_length=255, null=True, blank=True)
    UpdatedDate = models.DateTimeField(null=True, blank=True)
    TrainerId = models.ForeignKey(TrainingStaff, on_delete=models.CASCADE)



class ProofOfIdentty(models.Model):
    ID = models.AutoField(primary_key=True)
    Type = models.CharField(max_length=255)
    Value = models.CharField(max_length=255)
    CreatedBy = models.CharField(max_length=255)
    CreatedDate = models.DateTimeField(default=timezone.now)
    UpdatedBy = models.CharField(max_length=255)
    UpdatedDate = models.DateTimeField(default=timezone.now)

class TrainingBatches(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Course_details = models.ForeignKey(Courses, on_delete=models.CASCADE, null=True, blank=True)
    TrainerId = models.ForeignKey(TrainingStaff, on_delete=models.CASCADE, null=True, blank=True)
    MeetingURL = models.CharField(max_length=500)
    StartDate = models.DateField()
    EndDate = models.DateField()
    Duration = models.IntegerField()
    StartTime = models.TimeField()
    EndTime = models.TimeField()
    IsActive = models.BooleanField()
    CreatedBy = models.CharField(max_length=255)
    CreatedDate = models.DateTimeField(default=timezone.now)
    UpdatedDate = models.DateTimeField(default=timezone.now)
    UpdatedBy = models.CharField(max_length=255)

    def __str__(self):
        return self.Name

class StudentBatchAllocation(models.Model):
    ID = models.AutoField(primary_key=True)
    TrainerID = models.ForeignKey(TrainingStaff, on_delete=models.CASCADE)
    BatchID = models.ForeignKey(TrainingBatches, on_delete=models.CASCADE)
    CreatedBy = models.CharField(max_length=255)
    CreatedDate = models.DateTimeField(default=timezone.now)
    UpdatedBy = models.CharField(max_length=255, null=True, blank=True)
    UpdatedDate = models.DateTimeField(null=True, blank=True)

class StudentDetails(models.Model):
    ID = models.AutoField(primary_key=True)
    StudentID = models.ForeignKey(User, on_delete=models.CASCADE)
    BatchID = models.ForeignKey(TrainingBatches, on_delete=models.CASCADE)
    PaymentDetails = models.ForeignKey(Payments, on_delete=models.CASCADE, null=True, blank=True)
    CreatedBy = models.CharField(max_length=255)
    CreatedDate = models.DateTimeField(default=timezone.now)
    UpdatedBy = models.CharField(max_length=255, null=True, blank=True)
    UpdatedDate = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.StudentID.name)

class CourseStatus(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=255, null=True, blank=True)
    IsActive = models.BooleanField()
    CreatedBy = models.CharField(max_length=255)
    CreatedDate = models.DateTimeField(default=timezone.now)
    UpdatedBy = models.CharField(max_length=255)
    UpdatedDate = models.DateTimeField(default=timezone.now)

class StudentStudyMetirials(models.Model):
    StudyMaterialID = models.AutoField(primary_key=True)
    CourseID = models.ForeignKey(Courses, on_delete=models.CASCADE,null=True,blank=False)
    MaterialType =  models.CharField(max_length=100)
    File = models.FileField(upload_to='studymaterials')
    CreatedDate = models.DateTimeField(auto_now_add=True)
    UploadedBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploaded_student_studymaterials')
    createdby = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_student_studymaterials')
    uploadesdate = models.DateTimeField(auto_now_add=True)
    
