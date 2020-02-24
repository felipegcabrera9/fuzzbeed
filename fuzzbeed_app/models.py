from django.db import models
from login_app.models import User
# Create your models here.

class QuizManager(models.Manager):
    def quiz_validator(request, postdata):
        errors = {}
        if not len(postdata['name'] > 5):
            errors['name'] = 'Your quizes name must have more than five characters.'
        if not len(postdata['desc'] > 10):
            errors['desc'] = 'Your quiz must have a description of more than ten characters'
        for i in range len(postdata['outcomes']):
            if not len(postdata['outcomes'][i]) > 1:
                errors['outcomes'] = 'All your quiz outcomes must have at least two characters'
        return errors

class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    outcome = models.CharField(max_length = 25)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Quiz(models.Model):
    name = models.CharField(max_length = 255)
    desc = models.CharField(max_length = 255)
    outcomes = models.ArrayField(models.CharField(max_length = 1))
    users = models.ManyToManyField(User, through='Results')
    qadata = models.JSONfield()
    image = models.ImageField(upload_to='quiz_banner', blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = QuizManager()
    #needs to store an image
    #array of four possible outcomes for the quiz
