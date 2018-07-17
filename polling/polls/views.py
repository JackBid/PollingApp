from django.shortcuts import render
from .models import Question

# Create your views here.
def home(request):
    question_list = Question.objects.order_by('-pub_date')
    return render(request, 'polls/home.html', {'questions': question_list})
