from django.contrib import admin

# Register your models here.
from user.models import Doctor, Patient

admin.site.register(Doctor)
admin.site.register(Patient)
