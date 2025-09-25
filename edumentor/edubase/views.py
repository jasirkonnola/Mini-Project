from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Question
from .forms import QuestionForm


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

#CRUD Function
class QuestionListView(ListView):
    model = Question
    context_object_name = 'questions'
    template_name = 'questions.html'
    ordering = ['-created_at']

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category=category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['selected_category'] = self.request.GET.get('category', '')
        context['categories'] = dict(Question.CATEGORY_CHOICES)
        return context

class QuestionDetailView(DetailView):
    model = Question

class QuestionCreateView(CreateView):
    model = Question
    form_class = QuestionForm
    template_name = 'edubase/question_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)