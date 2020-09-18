from django.db import models
from user.models import Doctor, Patient
from django.utils import timezone

from utils import random_string


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    scheduled = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    token = models.CharField(auto_created=True, default=random_string, max_length=10, editable=False)

    def __str__(self):
        return self.token
