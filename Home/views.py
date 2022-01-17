import email
from django.shortcuts import render, redirect
from django.contrib import messages
from Home.models import Contact
# Create your views here.


def home(request):
    return render(request, 'Home/index.html')

def contact(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        message = request.POST['message']
        if request.user.is_authenticated:
            if request.user.email == email:    
                contact = Contact(full_name=full_name, email=email, message=message)
                contact.save()
                messages.success(request, "Message Sent Successfully!")
                return redirect("contact")
            else:
                messages.success(request, "Please Enter Your registered email address!")
                return redirect("contact")

        else:
            messages.warning(request, "Please login To Send Messages!")
            return redirect("login")


    return render(request, 'Home/contact.html')
