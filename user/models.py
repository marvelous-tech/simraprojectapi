from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL
TYPE_CHOICES = (
    ('S', 'SUPER_ADMIN'),
    ('A', 'ADMIN')
)


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor')
    dob = models.DateField(blank=True, null=True)
    doctor_license = models.CharField(max_length=255)
    address = models.TextField()
    mobile_no = models.CharField(max_length=20)
    email = models.EmailField()
    country = models.CharField(max_length=3, default='UK')
    documents = models.FileField(upload_to='FILES/')

    def __str__(self):
        return self.user.username


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient')
    dob = models.DateField(blank=True, null=True)
    address = models.TextField()
    mobile_no = models.CharField(max_length=20)
    email = models.EmailField()
    country = models.CharField(max_length=3, default='UK')
    documents = models.FileField(upload_to='FILES/')

    def __str__(self):
        return self.user.username


class Receptionist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='receptionist')
    dob = models.DateField(blank=True, null=True)
    address = models.TextField()
    mobile_no = models.CharField(max_length=20)
    email = models.EmailField()
    country = models.CharField(max_length=3, default='UK')
    documents = models.FileField(upload_to='FILES/')

    def __str__(self):
        return self.user.username


class Nurse(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='nurse')
    dob = models.DateField(blank=True, null=True)
    address = models.TextField()
    mobile_no = models.CharField(max_length=20)
    email = models.EmailField()
    country = models.CharField(max_length=3, default='UK')
    documents = models.FileField(upload_to='FILES/')

    def __str__(self):
        return self.user.username


class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='manager')
    dob = models.DateField(blank=True, null=True)
    address = models.TextField()
    mobile_no = models.CharField(max_length=20)
    email = models.EmailField()
    country = models.CharField(max_length=3, default='UK')
    documents = models.FileField(upload_to='FILES/')
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)

    def __str__(self):
        return self.user.username






