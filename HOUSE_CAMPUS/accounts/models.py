from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    STUDENT = "student"
    LANDLORD = "landlord"
    ADMIN = "admin"

    ROLE_CHOICES = [
        (STUDENT, "Student"),
        (LANDLORD, "Landlord"),
        (ADMIN, "Admin"),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=STUDENT
    )

    phone = models.CharField(
        max_length=20,
        blank=True
    )

    whatsapp_number = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        help_text="Example: 254712345678"
    )

    university = models.CharField(
        max_length=150,
        blank=True
    )

    county = models.CharField(
        max_length=100,
        blank=True
    )

    town = models.CharField(
        max_length=100,
        blank=True
    )

    profile_picture = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True
    )

    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username