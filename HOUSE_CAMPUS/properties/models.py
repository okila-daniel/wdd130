from django.db import models


class Property(models.Model):

    HOUSE_TYPES = [
        ("Bedsitter", "Bedsitter"),
        ("Single Room", "Single Room"),
        ("One Bedroom", "One Bedroom"),
        ("Two Bedroom", "Two Bedroom"),
        ("Hostel", "Hostel"),
    ]

    title = models.CharField(max_length=200)
    house_type = models.CharField(max_length=50, choices=HOUSE_TYPES)
    university = models.CharField(max_length=150)
    county = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.PositiveIntegerField(default=1)
    description = models.TextField()

    image = models.ImageField(
        upload_to="properties/",
        blank=True,
        null=True,
    )

    available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title