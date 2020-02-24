from django.db import models
import re
import datetime
import time
from datetime import timedelta


class UserManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = 'Invalid email address!'
        try:
            User.objects.get(id='user.id')
            errors['email'] = 'This email is already registered'
        except:
            pass
        if not NAME_REGEX.match(post_data['first_name']):
            errors['first_name'] = 'Invalid name'
        if not NAME_REGEX.match(post_data['last_name']):
            errors['last_name'] = 'Invalid name'
        if len(post_data['first_name']) < 2:
            errors['first_name'] = 'First name should be at least 2 characters'
        if len(post_data['last_name']) < 2:
            errors['last_name'] = 'Last name should be at least 2 characters'
        if len(post_data['password']) < 8:
            errors['password'] = 'Password is too short'
        if post_data['password'] != post_data['confirm_password']:
            errors['password'] = 'Passwords do not match'
        if len(post_data['birthdate']) == 0:
            errors['birthdate'] = 'Please enter your birthdate'
        else:
            today = datetime.datetime.now()
            birthdate = datetime.datetime.fromisoformat(post_data['birthdate'])
            if ((today - birthdate) < datetime.timedelta(13*365 + 3)):
                errors['birthdate'] = 'You are too young to use this website'
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    birthdate = models.DateTimeField()
    password = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

# Create your models here.
