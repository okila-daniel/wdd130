from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import MessageForm
from .models import Message
from properties.models import Property


@login_required
def send_message(request, pk):
    property = get_object_or_404(Property, pk=pk)

    if request.method == "POST":
        form = MessageForm(request.POST)

        if form.is_valid():
            msg = form.save(commit=False)
            msg.sender = request.user
            msg.receiver = property.landlord
            msg.property = property
            msg.save()

            messages.success(request, "Your message has been sent successfully!")

            return redirect("property_detail", pk=property.pk)

    else:
        form = MessageForm()

    return render(request, "messaging/send_message.html", {
        "form": form,
        "property": property,
    })


@login_required
def inbox(request):
    inbox_messages = Message.objects.filter(receiver=request.user)

    return render(request, "messaging/inbox.html", {
        "messages": inbox_messages
    })