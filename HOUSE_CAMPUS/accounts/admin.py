from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    list_display = (
        "username",
        "email",
        "role",
        "phone",
        "whatsapp_number",
        "verified",
        "is_staff",
    )

    list_filter = (
        "role",
        "verified",
        "is_staff",
        "is_superuser",
    )

    search_fields = (
        "username",
        "email",
        "phone",
        "whatsapp_number",
    )

    fieldsets = UserAdmin.fieldsets + (
        (
            "HOUSE CAMPUS",
            {
                "fields": (
                    "role",
                    "phone",
                    "whatsapp_number",
                    "university",
                    "county",
                    "town",
                    "profile_picture",
                    "verified",
                )
            },
        ),
    )