from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator

from .models import Property
from .forms import PropertyForm


def property_list(request):
    query = request.GET.get("q")
    county = request.GET.get("county")
    available = request.GET.get("available")
    max_price = request.GET.get("max_price")

    properties = Property.objects.all().order_by("-created_at")

    if query:
        properties = properties.filter(
            Q(title__icontains=query) |
            Q(university__icontains=query) |
            Q(town__icontains=query)
        )

    if county:
        properties = properties.filter(county__icontains=county)

    if max_price:
        properties = properties.filter(price__lte=max_price)

    if available == "yes":
        properties = properties.filter(available=True)

    paginator = Paginator(properties, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "properties/property_list.html",
        {
            "properties": page_obj,
            "page_obj": page_obj,
            "query": query,
            "county": county,
            "max_price": max_price,
            "available": available,
        },
    )


@login_required
def add_property(request):
    if request.user.role != "landlord":
        return redirect("property_list")

    if request.method == "POST":
        form = PropertyForm(request.POST, request.FILES)

        if form.is_valid():
            property = form.save(commit=False)
            property.landlord = request.user
            property.save()
            return redirect("property_list")

    else:
        form = PropertyForm()

    return render(
        request,
        "properties/add_property.html",
        {
            "form": form,
        },
    )


def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)

    return render(
        request,
        "properties/property_detail.html",
        {
            "property": property,
        },
    )


@login_required
def edit_property(request, pk):
    property = get_object_or_404(
        Property,
        pk=pk,
        landlord=request.user,
    )

    if request.method == "POST":
        form = PropertyForm(
            request.POST,
            request.FILES,
            instance=property,
        )

        if form.is_valid():
            form.save()
            return redirect("property_list")

    else:
        form = PropertyForm(instance=property)

    return render(
        request,
        "properties/edit_property.html",
        {
            "form": form,
            "property": property,
        },
    )


@login_required
def delete_property(request, pk):
    property = get_object_or_404(
        Property,
        pk=pk,
        landlord=request.user,
    )

    if request.method == "POST":
        property.delete()
        return redirect("property_list")

    return render(
        request,
        "properties/delete_property.html",
        {
            "property": property,
        },
    )