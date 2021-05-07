from django.db import models
import re
import bcrypt

email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def reg_validator(self, postData):
        errors = {}

        if len(postData['username']) < 5:
            errors["username"] = "Username should be atleast 5 characters long"
        user_username = User.objects.filter(username=postData['username'])
        if len(user_username) > 0:
            errors["username_duplicate"] = "Username already in use"        
        if len(postData['email']) == 0:
            errors["email"] = "You must enter an email"
        elif not email_regex.match(postData['email']):
            errors["email"] = "Your email must be valid"
        current_users = User.objects.filter(email=postData['email'])
        if len(current_users) > 0 :
            errors["duplicate"] = "Email input is already in use"
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters"
        if postData['password'] != postData['confirm_password']:
            errors['pw_match'] = "Password must match!"
        
        return errors

class User(models.Model):
    username = models.CharField(max_length=55)
    email = models.CharField(max_length=55)
    password = models.CharField(max_length=45)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    objects = UserManager()

class Pet(models.Model):
    name = models.CharField(max_length=55)
    breed = models.CharField(max_length=55)
    birthdate = models.DateField()
    age = models.IntegerField()
    fav_food = models.TextField()
    curr_weight = models.IntegerField()
    goal_weight = models.IntegerField()
    daily_feeding = models.IntegerField()
    owner = models.ForeignKey(User, related_name="owner", on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
# Create your models here.
