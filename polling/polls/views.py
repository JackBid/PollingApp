from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from .models import Choice

# Create your views here.
def home(request):
    questions = []
    for question in Question.objects.all():
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
