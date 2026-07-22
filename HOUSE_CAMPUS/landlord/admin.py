from django.contrib import admin
from .models import LandlordApplication


@admin.register(LandlordApplication)
class LandlordApplicationAdmin(admin.ModelAdmin):
    list_display = (
        "applicant",
        "phone",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "created_at",
    )

    search_fields = (
        "applicant__username",
        "phone",
        "national_id",
    )

    actions = ["approve_applications", "reject_applications"]

    def approve_applications(self, request, queryset):
        for application in queryset:
            application.status = "approved"
            application.save()

            user = application.applicant
            user.role = "landlord"
            user.verified = True
            user.save()

        self.message_user(
            request,
            f"{queryset.count()} application(s) approved."
        )

    approve_applications.short_description = "Approve selected applications"

    def reject_applications(self, request, queryset):
        queryset.update(status="rejected")

    reject_applications.short_description = "Reject selected applications"