from django.contrib import admin
from .models import Property


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "house_type",
        "university",
        "town",
        "price",
        "available",
    )

    list_filter = (
        "house_type",
        "county",
        "available",
    )

    search_fields = (
        "title",
        "town",
        "university",
    )

    list_editable = (
        "available",
    )

    ordering = (
        "title",
    )