from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from .models import Choice
from datetime import datetime

# Create your views here.
def home(request):
    questions = []
    for question in Question.objects.all().order_by('-pub_date'):
        temp_question = {}
        temp_question['title'] = question.question_text
        temp_question['pub_date'] = question.pub_date
        temp_question['id'] = question.id
        choicelist = list(Choice.objects.filter(question_id=question.id))
        temp_question['choices'] = choicelist
        questions.append(temp_question)
    return render(request, 'polls/home.html', {'questions':questions})

def vote(request):
    choice = request.GET.get('choice', None)
    choice = choice.capitalize()
    c = Choice.objects.get(choice_text=choice)
    c.votes += 1
    c.save()
    return HttpResponse(str(c.id) + " " + str(c.choice_text) + " " + str(c.votes))

def addQuestion(request):
    return render(request, 'polls/addQuestion.html')

def submitted(request):
    title = request.GET.get('title', None)
    question = Question.objects.create(question_text=title, pub_date=datetime.now())
    options = []
    for i in request.GET.lists():
        if 'option' in i[0]:
            print(i[1][0])
            Choice.objects.create(question=question, choice_text=i[1][0], votes=0)
    #option1 = request.GET.get('option-1', None)
    #option2 = request.GET.get('option-2', None)

    #choice1 = Choice.objects.create(question=question, choice_text=option1, votes=0)
    #choice2 = Choice.objects.create(question=question, choice_text=option2, votes=0)
    return render(request, 'polls/submitted.html')
