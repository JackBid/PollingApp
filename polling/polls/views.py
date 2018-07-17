from django.shortcuts import render
from .models import Question
from .models import Choice

# Create your views here.
def home(request):
    questions = []
    for question in Question.objects.all():
        temp_question = {}
        temp_question['title'] = question.question_text
        temp_question['pub_date'] = question.pub_date
        choicelist = list(Choice.objects.filter(question_id=question.id))
        temp_question['choices'] = choicelist
        questions.append(temp_question)
    return render(request, 'polls/home.html', {'questions':questions})
