from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User


class RegisterView(View):
    def get(self, request):
        return render(request, 'reg/register.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, password=password)
        auth_login(request, user)
        return redirect('login')


class LoginView(View):
    def get(self, request):
        return render(request, 'reg/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            return render(request, 'actions/food_list.html')

        # Add feedback if login fails (optional)
        return render(request, 'reg/login.html', {'error': 'Invalid credentials'})


class LogoutView(View):
    def post(self, request):
        auth_logout(request)
        return redirect('login')
