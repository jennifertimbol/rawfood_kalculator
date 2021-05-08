from django.shortcuts import render, redirect
from .models import User, Pet
from .forms import petForm, kalculatorForm
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, "home.html")

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
        'user' : User.objects.get(id=request.session['logged_user']),
        'petForm':petForm,
        
    }

    return render(request, "userprofile.html", context)

def petinfo(request):
    context = {
        'user' : User.objects.get(id=request.session['logged_user']),
        'petForm':petForm,
    }
    return render(request, 'petinfo.html', context)

def addpetinfo(request):
    if request.method == "POST":
        postedPetForm = petForm(request.POST, request.FILES)
        if postedPetForm.is_valid():
            postedPetForm.save()
            return redirect('/addpet')
        else:
            context = {
                'user' : User.objects.get(id=request.session['logged_user']),
                'petForm':postedPetForm,
            }
            return render(request, "petinfo.html", context)
    return redirect('/profile')

def addpet(request):
    if request.method== "POST":
        postedKalculatorForm = kalculatorForm(request.POST)
        if postedKalculatorForm.is_valid():
            goal_weight = request.GET['goal_weight']
            percentage = request.GET['percentage']
            results = goal_weight*percentage
            return redirect('/results')

    context = {
        'user' : User.objects.get(id=request.session['logged_user']),
        'kalculatorForm' : kalculatorForm,
    }
    return render(request, "calculate.html", context)

def results(request):
    context = {
        'user' : User.objects.get(id=request.session['logged_user']),
    }
    return render(request, "results.html", context)

def logout(request):
    request.session.flush()
    return redirect('/')
# Create your views here.
