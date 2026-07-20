from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm


def home(request):
    return render(request, "accounts/home.html")


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
        {"form": form},
    )


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password,
        )

        if user is not None:
            login(request, user)
            return redirect("dashboard")

        messages.error(request, "Invalid username or password.")

    return render(request, "accounts/login.html")


def dashboard(request):
    return render(request, "accounts/dashboard.html")