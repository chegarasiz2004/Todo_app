from django.contrib.auth import authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Plan

def todos(request):
    if request.user.is_authenticated:
        t1 = Plan.objects.filter(student=request.user)
        return render(request, 'todo.html', {"t1":t1})
    else:
        return redirect("/")
def loginView(request):
    if request.method == 'POST':
        users = authenticate(username=request.POST["login"], password=request.POST["password"])
        if users is None:
            return redirect("/")
        else:
            login(request, users)
            return redirect("/todos/")
    return render(request, "home.html")

def logoutView(request):
    logout(request)
    return redirect("/")


