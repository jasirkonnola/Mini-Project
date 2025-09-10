from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
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

class QuestionDetailView(DetailView):
    model = Question

class QuestionCreateView(CreateView):
    model = Question
    fields = ['title', 'content']
    template_name = 'edubase/question_form.html'  # Make sure this matches your actual template filename

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)