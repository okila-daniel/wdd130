from django.contrib import admin
from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):

    list_display = (
        "sender",
        "receiver",
        "property",
        "subject",
        "is_read",
        "created_at",
    )

    list_filter = (
        "is_read",
        "created_at",
    )

    search_fields = (
        "subject",
        "sender__username",
        "receiver__username",
    )

    ordering = (
        "-created_at",
    )