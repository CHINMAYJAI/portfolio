from django.shortcuts import render, redirect
from datetime import datetime
from WebApp.models import Contact

# Create your views here.


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def experience(request):
    return render(request, "experience.html")


def project1(request):
    return render(request, "project1.html")


def project2(request):
    return render(request, "project2.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        reason_to_contact = request.POST.get("reason_to_contact")
        if not Contact.objects.filter(name=name,email=email,reason_to_contact=reason_to_contact).exists():
            contact = Contact(
                name=name,
                email=email,
                reason_to_contact=reason_to_contact,
                date=datetime.today(),
            )
            contact.save()
        return redirect("thanking_page")  # Redirect to the thanking page URL name

    return render(request, "contact.html")


def thankingPage(request):
    return render(request, "thanking_page.html")
