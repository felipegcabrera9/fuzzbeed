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
        for i in range(4):
            if not len(postdata['outcomes'][i]) > 1:
                errors['outcomes'] = 'All your quiz outcomes must have at least two characters'
        for i in range(10):
            if not len(postdata['questions'][i]) > 10:
                errors['questions'] = 'all your quesions must be at least ten characters long'
        for i in range(40):
            if not len(postdata['answers'][i]) > 10:
                errors['answers'] = 'Your quizes answers must all have at least ten characters'
        return errors


class Quiz(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    users = models.ManyToManyField(User, through='Result')
    image = models.ImageField(upload_to='quiz_banner', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = QuizManager()
    # four possible outcomes
    o1 = models.CharField(max_length=50)
    o2 = models.CharField(max_length=50)
    o3 = models.CharField(max_length=50)
    o4 = models.CharField(max_length=50)
    # ten questions
    q1 = models.CharField(max_length=50)
    q2 = models.CharField(max_length=50)
    q3 = models.CharField(max_length=50)
    q4 = models.CharField(max_length=50)
    q5 = models.CharField(max_length=50)
    q6 = models.CharField(max_length=50)
    q7 = models.CharField(max_length=50)
    q8 = models.CharField(max_length=50)
    q9 = models.CharField(max_length=50)
    q10 = models.CharField(max_length=50)
    # four possible answers for each question
    q1a1 = models.CharField(max_length=50)
    q1a2 = models.CharField(max_length=50)
    q1a3 = models.CharField(max_length=50)
    q1a4 = models.CharField(max_length=50)
    q2a1 = models.CharField(max_length=50)
    q2a2 = models.CharField(max_length=50)
    q2a3 = models.CharField(max_length=50)
    q2a4 = models.CharField(max_length=50)
    q3a1 = models.CharField(max_length=50)
    q3a2 = models.CharField(max_length=50)
    q3a3 = models.CharField(max_length=50)
    q3a4 = models.CharField(max_length=50)
    q4a1 = models.CharField(max_length=50)
    q4a2 = models.CharField(max_length=50)
    q4a3 = models.CharField(max_length=50)
    q4a4 = models.CharField(max_length=50)
    q5a1 = models.CharField(max_length=50)
    q5a2 = models.CharField(max_length=50)
    q5a3 = models.CharField(max_length=50)
    q5a4 = models.CharField(max_length=50)
    q6a1 = models.CharField(max_length=50)
    q6a2 = models.CharField(max_length=50)
    q6a3 = models.CharField(max_length=50)
    q6a4 = models.CharField(max_length=50)
    q7a1 = models.CharField(max_length=50)
    q7a2 = models.CharField(max_length=50)
    q7a3 = models.CharField(max_length=50)
    q7a4 = models.CharField(max_length=50)
    q8a1 = models.CharField(max_length=50)
    q8a2 = models.CharField(max_length=50)
    q8a3 = models.CharField(max_length=50)
    q8a4 = models.CharField(max_length=50)
    q9a1 = models.CharField(max_length=50)
    q9a2 = models.CharField(max_length=50)
    q9a3 = models.CharField(max_length=50)
    q9a4 = models.CharField(max_length=50)
    q10a1 = models.CharField(max_length=50)
    q10a2 = models.CharField(max_length=50)
    q10a3 = models.CharField(max_length=50)
    q10a4 = models.CharField(max_length=50)


class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    outcome = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
