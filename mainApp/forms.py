from django import forms
from .models import Pet, User

# class userForm(forms.Form):
#     username = forms.CharField(max_length=55, min_length=5)
#     email = forms.CharField(max_length=55)
#     password = forms.CharField(max_length=45, min_length=8)

class petForm(forms.ModelForm):
    # name = forms.CharField(max_length=55, min_length=2)
    # breed = forms.CharField(max_length=55, min_length=5)
    # birthdate = forms.DateField()
    # age = forms.IntegerField()
    # fav_food = forms.CharField(max_length=300, min_length=5)
    # profile_pic = forms.ImageField()
    # curr_weight = forms.IntegerField()
    # goal_weight = forms.IntegerField()
    # daily_feeding = forms.IntegerField()
    # owner = forms.ModelChoiceField(queryset=User.objects.get(id=request.session['logged_user']))
    class Meta:
        model = Pet
        fields = ['name', 'breed', 'birthdate', 'age', 'fav_food', 'profile_photo', 'curr_weight', 'goal_weight', 'percentage', 'daily_feeding']
        labels = {
            'fav_food' : "Favorite food:",
            'birthdate' : "Birthday (mm/dd/yyyy):",
            'curr_weight' : "Current weight (lbs):",
            'goal_weight' : "Goal weight (lbs):",
            'daily_feeding' : "How many times a day do you feed your pet?"
        }
    
# class calculatorForm(forms.ModelForm):
#     class Meta:
#         model = Pet
#         fields = ['curr_weight', 'goal_weight', 'percentage', 'daily_feeding']
#         labels = {
        
#         }