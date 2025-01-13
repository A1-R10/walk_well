from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        passw = request.POST.get("password")

        user = authenticate(username=username, password=passw)

        if user is None:
            messages.error(request, 'Invalid Login')
            return redirect('accounts:login')
        else:
            login(request, user)
            return redirect('home')
    return render(request, 'user_authentication/login.html')