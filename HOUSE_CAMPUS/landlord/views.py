from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import LandlordApplicationForm


@login_required
def apply_landlord(request):

    if request.method == "POST":
        form = LandlordApplicationForm(
            request.POST,
            request.FILES,
        )

        if form.is_valid():
            application = form.save(commit=False)
            application.applicant = request.user
            application.save()

            return redirect("dashboard")

    else:
        form = LandlordApplicationForm()

    return render(
        request,
        "landlord/apply.html",
        {
            "form": form,
        },
    )