from django.db import models
import json
from login_app.models import User
from jsonfield import JSONField
# Create your models here.


class QuizManager(models.Manager):
    def quiz_validator(request, postdata):
        errors = {}
        if not len(postdata['name'] > 5):
            errors['name'] = 'Quiz name must have more than five characters'
        if not len(postdata['desc'] > 10):
            errors['desc'] = 'Quiz must have a description of more than ten characters'
        for i in range(4):
            if not len(postdata['outcomes'][i]) > 1:
                errors['outcomes'] = 'Quiz outcomes must have at least two characters'
        for i in range(10):
            if not len(postdata['questions'][i]) > 10:
                errors['questions'] = 'Questions must be at least ten characters long'
        for i in range(40):
            if not len(postdata['answers'][i]) > 10:
                errors['answers'] = 'Quiz answers must have at least ten characters'
        return errors


class Quiz(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    users = models.ManyToManyField(User, through='Result')
    image = models.ImageField(upload_to='quiz_banner', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = QuizManager()
    o1 = models.CharField(max_length=50)
    o2 = models.CharField(max_length=50)
    o3 = models.CharField(max_length=50)
    o4 = models.CharField(max_length=50)
    # ten questions and four possible answers for each question
    qna = JSONField()


class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    outcome = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
