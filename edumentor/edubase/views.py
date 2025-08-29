from django.shortcuts import render
from django.views.generic import ListView
from .models import Question


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

#CRUD Function
class QuestionListView(ListView):
    model = Question
    context_object_name = 'questions'
    template_name = 'questions.html'  # Make sure this matches your actual template filename
    ordering = ['-created_at']  # Orders questions by creation date, newest first+