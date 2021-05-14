from django.shortcuts import render, redirect
from .models import User, Pet
from .forms import petForm, secondPetForm
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, "home.html")

def register(request):
    return render(request, "register2.html")

def login(request):
    return render(request, "login2.html")

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
            print(form.id)
            form.save()
            return redirect(f'/rawfoodkalculator/results/{form.id}')
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

def results(request, pet_id):

    user = User.objects.get(id=request.session['logged_user'])
    curr_pet = Pet.objects.get(id=pet_id)

    pet_weight = curr_pet.goal_weight
    percent = curr_pet.percentage
    total = float(pet_weight) * float(percent)

    meat = total * .8
    bone = total * .1
    liver = total * .05
    other = total * .05

    context= {
        'user':user,
        'pet':curr_pet,
        'total':round(total, 10),
        'meat': round(meat, 10),
        'bone': round(bone, 10),
        'liver': round(liver, 10),
        'other': round(other, 10),
    }
    return render(request, "results.html", context)

def deletepet(request, pet_id):
    if 'logged_user' not in request.session:
        return redirect('/')
    
    delete_pet = Pet.objects.get(id=pet_id)
    delete_pet.delete()
    return redirect('/profile')

def updatepet(request, pet_id):
    if "logged_user" not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['logged_user'])
    curr_pet = Pet.objects.get(id=pet_id)

    context = {
        'user':user,
        'pet':curr_pet,
        'secondPetForm':secondPetForm()
    } 
    return render(request, 'updatepet.html', context)

def update(request, pet_id):
    if request.method == 'POST':
        owner = User.objects.get(id=request.session['logged_user'])
        current_pet = Pet.objects.get(id=pet_id)
        postedSecondForm = secondPetForm(request.POST, instance=current_pet)
        if postedSecondForm.is_valid():
            form = postedSecondForm.save()
    else:
        context = {
        'user':owner,
        'pet':current_pet,
        'secondPetForm':secondPetForm()
    } 
        return render(request, 'updatepet.html', context)
        
    return redirect(f'/rawfoodkalculator/results/{current_pet.id}')

def logout(request):
    request.session.flush()
    return redirect('/')
# Create your views here.
