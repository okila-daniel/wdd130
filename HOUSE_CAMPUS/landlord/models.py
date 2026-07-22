from django.db import models
from django.conf import settings


class LandlordApplication(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
    ]

    applicant = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="landlord_application",
    )

    phone = models.CharField(max_length=20)
    national_id = models.CharField(max_length=50)
    university = models.CharField(max_length=150)
    county = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    number_of_properties = models.PositiveIntegerField()

    id_document = models.FileField(
        upload_to="landlord_documents/"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending",
    )

    admin_notes = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.applicant.username} - {self.status}"