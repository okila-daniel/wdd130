from django.db import models
from django.conf import settings
from properties.models import Property


class Message(models.Model):
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="sent_messages",
    )

    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="received_messages",
    )

    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name="messages",
    )

    subject = models.CharField(max_length=200)

    message = models.TextField()

    is_read = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.sender} → {self.receiver} ({self.property.title})"