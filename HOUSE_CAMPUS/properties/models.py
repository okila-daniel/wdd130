from django.db import models
from django.conf import settings


class Property(models.Model):

    HOUSE_TYPES = [
        ("Bedsitter", "Bedsitter"),
        ("Silver House (Mabati)", "Silver House (Mabati)"),
        ("Hostel", "Hostel"),
        ("One Bedroom", "One Bedroom"),
        ("Two Bedroom", "Two Bedroom"),
        ("Shared Room", "Shared Room"),
        ("Self Contained", "Self Contained"),
    ]

    landlord = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="properties",
        null=True,
        blank=True,
    )

    title = models.CharField(max_length=200)

    house_type = models.CharField(
        max_length=50,
        choices=HOUSE_TYPES,
    )

    university = models.CharField(max_length=150)

    county = models.CharField(max_length=100)

    town = models.CharField(max_length=100)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    bedrooms = models.PositiveIntegerField(default=1)

    bathrooms = models.PositiveIntegerField(default=1)

    description = models.TextField()

    image = models.ImageField(
        upload_to="properties/",
        blank=True,
        null=True,
    )

    wifi = models.BooleanField(default=False)

    water = models.BooleanField(default=True)

    electricity = models.BooleanField(default=True)

    parking = models.BooleanField(default=False)

    distance_to_university = models.PositiveIntegerField(
        default=5,
        help_text="Distance to the university (minutes)",
    )

    available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title