from django.db import models
from user.models import Doctor, Patient, Receptionist
from django.utils import timezone

from utils import random_string

TYPE_CHOICES = (
    ('U', 'URGENT_APPOINTMENT'),
    ('R', 'ROUTINE_APPOINTMENT'),
    ('H', 'HOME_VISIT_APPOINTMENT')
)


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    receptionist = models.ForeignKey(Receptionist, on_delete=models.CASCADE, related_name='appointments')
    scheduled = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    token = models.CharField(auto_created=True, default=random_string, max_length=10, editable=False, unique=True)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)

    def __str__(self):
        return self.token
