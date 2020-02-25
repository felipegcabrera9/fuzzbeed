from django.shortcuts import render, redirect
from login_app.models import User
from .models import *


def new(request):
    return render(request, 'new.html')


def profile(request):
    if not 'id' in request.session:
        messages.error(request, 'Please login')
        return redirect('/')

    else:
        return render(request, 'profile.html')


def quiz(request):
    return render(request, 'quiz.html')


def rankings(request):
    return render(request, 'rankings.html')


def takeQuiz(request, quiz_id):
    # this block tallys the scores for each outcome
    # each index in the outcomes array is used to represent one of the four quiz outcomes
    # this loop increments indexes in the array based on the answers that came through the form
    outcomes = [0, 0, 0, 0]
    for key in request.post['answers']:
        if key == 'o1':
            outcomes[0] += 1
        elif key == 'o2':
            outcomes[1] += 1
        elif key == 'o3':
            outcomes[2] += 1
        else:
            outcomes[3] += 1
    # finds which outcome had the most points by indentify the index with the highest value in the outcomes array
    maxIndex = 0
    for i in range(len(outcomes)):
        max = outcomes[0]
        if outcomes[i] > max:
            max = outcomes[i]
            maxIndex = i
    # uses the data we found above to assign a relevant quiz outcome value to be sent to the results table
    quiz = Quiz.objects.get(id=quiz_id)
    if(maxIndex == 0):
        outcome = quiz.o1
    elif(maxIndex == 1):
        outcome = quiz.o2
    elif(maxIndex == 2):
        outcome = quiz.o3
    else:
        outcome = quiz.o4

    Result.objects.create(
        quiz=quiz,
        user=User.objects.get(id=request.session['user_id']),
        outcome=outcome
    )
    return redirect('profile')


def createQuiz(request):

    # storing questions in variables to be used as keys in the object
    q1 = request.post['q1']
    q2 = request.post['q2']
    q3 = request.post['q3']
    q4 = request.post['q4']
    q5 = request.post['q5']
    q6 = request.post['q6']
    q7 = request.post['q7']
    q8 = request.post['q8']
    q9 = request.post['q9']
    q10 = request.post['q10']

    # constructing objects that will be passed in when creating the Quiz instance
    qna = {
        q1: [
            request.post['q1a1'],
            request.post['q1a2'],
            request.post['q1a3'],
            request.post['q1a4']
        ],
        q2: [
            request.post['q2a1'],
            request.post['q2a2'],
            request.post['q2a3'],
            request.post['q2a4']
        ],
        q3: [
            request.post['q3a1'],
            request.post['q3a2'],
            request.post['q3a3'],
            request.post['q3a4']
        ],
        q4: [
            request.post['q4a1'],
            request.post['q4a2'],
            request.post['q4a3'],
            request.post['q4a4']
        ],
        q5: [
            request.post['q5a1'],
            request.post['q5a2'],
            request.post['q5a3'],
            request.post['q5a4']
        ],
        q6: [
            request.post['q6a1'],
            request.post['q6a2'],
            request.post['q6a3'],
            request.post['q6a4']
        ],
        q7: [
            request.post['q7a1'],
            request.post['q7a2'],
            request.post['q7a3'],
            request.post['q7a4']
        ],
        q8: [
            request.post['q8a1'],
            request.post['q8a2'],
            request.post['q8a3'],
            request.post['q8a4']
        ],
        q9: [
            request.post['q9a1'],
            request.post['q9a2'],
            request.post['q9a3'],
            request.post['q9a4']
        ],
        q10: [
            request.post['q10a1'],
            request.post['q10a2'],
            request.post['q10a3'],
            request.post['q10a4']
        ]
    }

    json_input = json.loads(qna)
    print(json_input)

    Quiz.objects.create(
        name=request.post['name'],
        desc=request.post['desc'],
        image=request.post['image'],
        o1=request.post['o1'],
        o2=request.post['o2'],
        o3=request.post['o3'],
        o4=request.post['o4'],
        qna=json_input
    )

    return redirect('profile')
