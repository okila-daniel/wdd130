from django.contrib import admin
from .models import Property, PropertyImage


class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1


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

    inlines = [PropertyImageInline]


@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    list_display = (
        "property",
        "uploaded_at",
    )

    search_fields = (
        "property__title",
    )

    ordering = (
        "-uploaded_at",
    )