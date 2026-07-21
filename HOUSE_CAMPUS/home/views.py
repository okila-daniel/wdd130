from django.shortcuts import render
from properties.models import Property


def home(request):
    featured_properties = Property.objects.filter(
        available=True
    ).order_by("-created_at")[:6]

    total_properties = Property.objects.count()

    available_properties = Property.objects.filter(
        available=True
    ).count()

    context = {
        "featured_properties": featured_properties,
        "total_properties": total_properties,
        "available_properties": available_properties,
    }

    return render(request, "home/index.html", context)