from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import StudentRegistrationForm, ProfileForm
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
            messages.success(request, "Account created successfully.")
            return redirect("login")

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

            if hasattr(user, "role") and user.role == "landlord":
                return redirect("/dashboard/")

            return redirect("/accounts/dashboard/")

        messages.error(request, "Invalid username or password.")

    return render(request, "accounts/login.html")


@login_required
def dashboard(request):
    return render(
        request,
        "accounts/dashboard.html",
    )


@login_required
def profile(request):

    if request.method == "POST":

        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=request.user
        )

        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("profile")

    else:

        form = ProfileForm(instance=request.user)

    return render(
        request,
        "accounts/profile.html",
        {
            "form": form,
        },
    )
from django.contrib.auth import logout
from django.shortcuts import redirect


def logout_user(request):
    logout(request)
    return redirect("home")