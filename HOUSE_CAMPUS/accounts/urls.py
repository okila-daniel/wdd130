from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path(
        "register/student/",
        views.register_student,
        name="register_student",
    ),

    path(
        "login/",
        views.login_user,
        name="login",
    ),

    path(
        "logout/",
        views.logout_user,
        name="logout",
    ),

    path(
        "dashboard/",
        views.dashboard,
        name="dashboard",
    ),

    path(
        "profile/",
        views.profile,
        name="profile",
    ),
]