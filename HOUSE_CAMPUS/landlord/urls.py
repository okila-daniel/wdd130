from django.urls import path
from . import views

urlpatterns = [
    path(
        "apply/",
        views.apply_landlord,
        name="apply_landlord",
    ),
]