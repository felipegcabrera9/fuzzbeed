from django.shortcuts import render, redirect
from login_app.models import *
from .models import *


def new(request):
    return render(request, 'new.html')


def profile(request):
    if not 'id' in request.session:
        messages.error(request, 'Please login')
        return redirect('/')

    else:
        return render(request, 'profile.html')


def quizpage(request, quiz_id):
    test_quiz = Quiz.objects.get(id=quiz_id)
    context = {'test_quiz': test_quiz}
    print(type(test_quiz.qna))
    for key in test_quiz.qna:
        print(key)
        print(test_quiz.qna[key])
    return render(request, 'quiz.html', context)


def rankings(request):
    return render(request, 'rankings.html')


def takeQuiz(request, quiz_id):
    # this block tallys the scores for each outcome
    # each index in the outcomes array is used to represent one of the four quiz outcomes
    # this loop increments indexes in the array based on the answers that came through the form
    outcomes = [0, 0, 0, 0]
    print(request.POST.getlist('answers'))
    for item in request.POST.getlist('answers'):
        print(item)
        if item == 'Choose...':
            pass
        elif item == '1':
            outcomes[0] += 1
        elif item == '2':
            outcomes[1] += 1
        elif item == '3':
            outcomes[2] += 1
        elif item == '4':
            outcomes[3] += 1

    print('outcomes:', outcomes)
    # finds which outcome had the most points by indentify the index with the highest value in the outcomes array
    maxIndex = 0
    for i in range(len(outcomes)):
        max = outcomes[0]
        if outcomes[i] > max:
            max = outcomes[i]
            maxIndex = i
    print(maxIndex)
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
        user=User.objects.get(id=request.session['id']),
        outcome=outcome
    )
    return redirect('profile')


def createQuiz(request):
    print('function hit')

    # storing questions in variables to be used as keys in the object
    q1 = request.POST['q1']
    q2 = request.POST['q2']
    q3 = request.POST['q3']
    q4 = request.POST['q4']
    q5 = request.POST['q5']
    q6 = request.POST['q6']
    q7 = request.POST['q7']
    q8 = request.POST['q8']
    q9 = request.POST['q9']
    q10 = request.POST['q10']

    # constructing objects that will be passed in when creating the Quiz instance
    qna = f"""{{
        "{request.POST['q1']}": [
            "{request.POST['q1a1']}",
            "{request.POST['q1a2']}",
            "{request.POST['q1a3']}",
            "{request.POST['q1a4']}"
        ],
        "{request.POST['q2']}": [
            "{request.POST['q2a1']}",
            "{request.POST['q2a2']}",
            "{request.POST['q2a3']}",
            "{request.POST['q2a4']}"
        ],
        "{request.POST['q3']}": [
            "{request.POST['q3a1']}",
            "{request.POST['q3a2']}",
            "{request.POST['q3a3']}",
            "{request.POST['q3a4']}"
        ],
        "{request.POST['q4']}": [
            "{request.POST['q4a1']}",
            "{request.POST['q4a2']}",
            "{request.POST['q4a3']}",
            "{request.POST['q4a4']}"
        ],
        "{request.POST['q5']}": [
            "{request.POST['q5a1']}",
            "{request.POST['q5a2']}",
            "{request.POST['q5a3']}",
            "{request.POST['q5a4']}"
        ],
        "{request.POST['q6']}": [
            "{request.POST['q6a1']}",
            "{request.POST['q6a2']}",
            "{request.POST['q6a3']}",
            "{request.POST['q6a4']}"
        ],
        "{request.POST['q7']}": [
            "{request.POST['q7a1']}",
            "{request.POST['q7a2']}",
            "{request.POST['q7a3']}",
            "{request.POST['q7a4']}"
        ],
        "{q8}": [
            "{request.POST['q8a1']}",
            "{request.POST['q8a2']}",
            "{request.POST['q8a3']}",
            "{request.POST['q8a4']}"
        ],
        "{q9}": [
            "{request.POST['q9a1']}",
            "{request.POST['q9a2']}",
            "{request.POST['q9a3']}",
            "{request.POST['q9a4']}"
        ],
        "{q10}": [
            "{request.POST['q10a1']}",
            "{request.POST['q10a2']}",
            "{request.POST['q10a3']}",
            "{request.POST['q10a4']}"
        ]
    }}"""

    print(qna)
    print(type(qna))

    json_input = json.loads(qna)
    print(json_input)

    Quiz.objects.create(
        name=request.POST['name'],
        desc=request.POST['desc'],
        image=request.POST['quiz_img'],
        o1=request.POST['o1'],
        o2=request.POST['o2'],
        o3=request.POST['o3'],
        o4=request.POST['o4'],
        qna=json_input
    )

    return redirect('/quiz/profile')
