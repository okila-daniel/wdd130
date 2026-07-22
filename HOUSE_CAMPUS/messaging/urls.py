from django.urls import path
from . import views

urlpatterns = [
    path("send/<int:pk>/", views.send_message, name="send_message"),
    path("inbox/", views.inbox, name="inbox"),
]