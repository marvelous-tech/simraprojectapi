from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(blank=True, null=True)
    doctor_license = models.CharField(max_length=255)
    address = models.TextField()
    mobile_no = models.CharField(max_length=20)
    email = models.EmailField()
    country = models.CharField(max_length=3, default='UK')
    documents = models.FileField(upload_to='FILES/')

    def __str__(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(blank=True, null=True)
    address = models.TextField()
    mobile_no = models.CharField(max_length=20)
    email = models.EmailField()
    country = models.CharField(max_length=3, default='UK')
    documents = models.FileField(upload_to='FILES/')

    def __str__(self):
        return self.name
