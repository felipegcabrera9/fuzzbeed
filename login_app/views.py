from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import User
import datetime


def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'login_page.html')


def register(request):

    errors = User.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], birthdate=request.POST['birthdate'], password=bcrypt.hashpw(
            request.POST['password'].encode(), bcrypt.gensalt()).decode())
        user.save()
        request.session['nick_name'] = user.first_name
        request.session['id'] = user.id
    return redirect('/quiz/profile')


def login(request):
    users = User.objects.filter(email=request.POST['email'])
    if len(users) == 0:
        messages.error(request, 'Email is incorrect')
        return redirect('/home')
    if len(users) >= 1:
        logged_user = users[0]

        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):

            request.session['nick_name'] = logged_user.first_name

            request.session['id'] = logged_user.id

            return redirect('/quiz/profile')
    return redirect('/home')


def logout(request):
    request.session.clear()
    return redirect('/')


# def login(request):
