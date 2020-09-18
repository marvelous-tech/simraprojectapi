from django.db import models

from user.models import Patient


class Subscription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='subscription')
