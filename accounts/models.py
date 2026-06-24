from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Defining a TextChoices class grouping our system user segments
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        DOCTOR = 'DOCTOR', 'Doctor'
        PATIENT = 'PATIENT', 'Patient'

    # Set the fallback default base role configuration to Admin
    base_role = Role.ADMIN

    role = models.CharField(
        max_length=15, 
        choices=Role.choices, 
        default=base_role
    )
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"