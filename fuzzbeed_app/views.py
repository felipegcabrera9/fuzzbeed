from django.shortcuts import render, redirect


def create(request):
    return render(request, 'create.html')


def profile(request):
    return render(request, 'profile.html')


def quiz(request):
    return render(request, 'quiz.html')


def rankings(request):
    return render(request, 'rankings.html')