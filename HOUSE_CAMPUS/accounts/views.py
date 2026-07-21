from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import StudentRegistrationForm
from properties.models import Property


def home(request):
    properties = Property.objects.filter(available=True)

    return render(
        request,
        "accounts/home.html",
        {
            "properties": properties,
        },
    )


def register_student(request):
    if request.method == "POST":
        form = StudentRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("home")

    else:
        form = StudentRegistrationForm()

    return render(
        request,
        "accounts/register_student.html",
        {
            "form": form,
        },
    )


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password,
        )

        if user is not None:
            login(request, user)

            # Redirect landlords to the landlord dashboard
            if hasattr(user, "role") and user.role == "landlord":
                return redirect("/dashboard/")

            # Redirect students to their dashboard
            return redirect("/accounts/dashboard/")

        messages.error(request, "Invalid username or password.")

    return render(request, "accounts/login.html")


def dashboard(request):
    return render(
        request,
        "accounts/dashboard.html",
    )