from django import forms
from .models import Pet

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
    class Meta:
        model = Pet
        fields = ['name', 'breed', 'birthdate', 'age', 'fav_food', 'profile_photo']
        labels = {
            'fav_food' : "Favorite food:",
            'birthdate' : "Birthday:"
        }
    
class kalculatorForm(forms.ModelForm):
    class Meta:
        model: Pet
        fields = ['curr_weight', 'goal_weight', 'percentage', 'daily_feeding']
        labels = {
            'curr_weight' : "Current weight:",
            'goal_weight' : "Goal weight: (lbs)",
            'daily_feeding' : "How many times a day do you feed your pet?"
        }