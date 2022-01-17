from django.shortcuts import render, redirect
from Accounts.models import Account
from django.contrib.auth.models import auth
from django.contrib import messages

# Create your views here.

def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            user_name = request.POST['user_name']
            user_email = request.POST['user_email']
            user_password1 = request.POST['user_password1']
            user_password2 = request.POST['user_password2']
            if user_password1 == user_password2:
                user = Account.objects.create_user(email=user_email, username=user_name, password=user_password1)
                user.save()
                if user is not None:
                    auth.login(request, user)
                    messages.success(request, "Successfully Logged In !")
                    return redirect("/")


        return render(request, "Accounts/signup.html")
    else:
        return redirect("home")


def login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            useremail = request.POST['useremail']
            userpassword = request.POST['userpassword']
            user = auth.authenticate(email=useremail, password=userpassword)
            if user is not None:
                auth.login(request, user)
                messages.success(request, "Successfully Logged In !")
                return redirect("/")

        return render(request, "Accounts/login.html")
    else:
        return redirect("home")

def logout(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            auth.logout(request)
            messages.warning(request, "Successfully Logged Out !")
            return redirect("login")
    else:
        return redirect('login')
