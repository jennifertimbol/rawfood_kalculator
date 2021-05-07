from django.shortcuts import render, redirect
from .models import User, Pet
from django.contrib import messages
import bcrypt

def index(request):
    if "logged_user" not in request.session:
        return redirect('/')
    context = {
        'user' : User.objects.get(id=request.session['logged_user'])
    }
    return render(request, "home.html", context)

def register(request):
    return render(request, "register.html")

def login(request):
    return render(request, "login.html")

def createaccount(request):
        if request.method == 'POST':
            errors = User.objects.reg_validator(request.POST)
            if len(errors) > 0:
                for key,value in errors.items():
                    messages.error(request, value)
                return redirect('/register')

        hash_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()

        user = User.objects.create(
            username = request.POST['username'],
            email = request.POST['email'],
            password = hash_pw
        )
        request.session['logged_user'] = user.id
        return redirect('/profile')

def signin(request):
    if request.method == "POST":
        user = User.objects.filter(username = request.POST['username'])

        if user:
            log_user = user[0]

            if bcrypt.checkpw(request.POST['password'].encode(), log_user.password.encode()):
                request.session['logged_user'] = log_user.id
                return redirect('/profile')
        messages.error(request, "username or password are incorrect.")
    return redirect('/login')

def userprofile(request):
    if "logged_user" not in request.session:
        return redirect('/')

    context = {
        'user' : User.objects.get(id=request.session['logged_user'])
    }

    return render(request, "userprofile.html", context)

def kalculator(request):
    if "logged user" not in request.session:
        return redirect('/')

    context = {
        'user' : User.objects.get(id=request.session['logged_user'])
    }

    return render(request, 'kalculator.html', context)

def logout(request):
    request.session.flush()
    return redirect('/')
# Create your views here.
