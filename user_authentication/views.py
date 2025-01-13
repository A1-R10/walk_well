from django.contrib.auth import authenticate, login ,logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        passw = request.POST.get("password")

        user = authenticate(username=username, password=passw)

        if user is None:
            # If authentication failed
            messages.error(request, 'Invalid Login')
            return redirect('accounts:login')
        else:
            #If authentication is successful
            login(request, user)
            return redirect('home')
    return render(request, 'user_authentication/login.html')

def user_register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # check if user already exist
        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request, 'Username already exist!')
            return redirect('authentication:register')
        
        # create new user object with provided info
        user = User.objects.create_user(first_name=first_name,
                                        last_name=last_name,
                                        username=username,
                                        email=email,
                                        password=password)
        
        # save user password 
        user.set_password(password)
        user.save()

        messages.info(request, 'Account created successfully!')
        return redirect('home')
    
    return render(request, 'user_authentication/register.html')