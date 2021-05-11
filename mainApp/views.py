from django.shortcuts import render, redirect
from .models import User, Pet
from .forms import petForm
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
    user = User.objects.get(id=request.session['logged_user'])
    allPets = Pet.objects.filter(owner_id=user.id)
    context = {
        'current_user' : User.objects.get(id=request.session['logged_user']),
        'allPets':allPets,       
    }
    return render(request, "userprofile.html", context)

def petinfo(request):
    context = {
        'user' : User.objects.get(id=request.session['logged_user']),
        'petForm':petForm(),
    }
    return render(request, 'petinfo.html', context)

def addpetinfo(request):
    if request.method == "POST":
        owner = User.objects.get(id=request.session['logged_user'])
        print(owner)
        postedPetForm = petForm(request.POST, request.FILES)
        print(request.POST)
        if postedPetForm.is_valid():
            print('Its valid!')
            form = postedPetForm.save(commit=False)
            print(owner.id)
            form.owner_id = owner.id
            form.save()
            return redirect('/rawfoodkalculator/results')
    else:
        context = {
            'user' : User.objects.get(id=request.session['logged_user']),
            'petForm':postedPetForm,
        }
        return render(request, "petinfo.html", context)
    return redirect('/profile')

# def addpet(request):
#     context = {
#         'user' : User.objects.get(id=request.session['logged_user']),
#         'calculatorForm':calculatorForm,
#     }
#     return render(request, "calculate.html", context)

def results(request):
    user = User.objects.get(id=request.session['logged_user'])
    allPets = Pet.objects.filter(owner_id=user.id)
    context= {
        'user':user,
        'allPets':allPets
    }
    return render(request, "results.html", context)

def logout(request):
    request.session.flush()
    return redirect('/')
# Create your views here.
