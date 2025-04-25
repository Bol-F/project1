from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, password=password)
        auth_login(request, user)
        return redirect('login')

    return render(request, 'reg/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            return render(request, 'actions/food_list.html')

    return render(request, 'reg/login.html')


def logout(request):
    auth_logout(request)
    return redirect('login')
