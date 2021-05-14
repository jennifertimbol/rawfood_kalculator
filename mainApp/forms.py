from django import forms
from .models import Pet, User

# class userForm(forms.Form):
#     username = forms.CharField(max_length=55, min_length=5)
#     email = forms.CharField(max_length=55)
#     password = forms.CharField(max_length=45, min_length=8)

class petForm(forms.ModelForm):
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

class secondPetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['curr_weight', 'goal_weight', 'percentage', 'daily_feeding']
        labels = {
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