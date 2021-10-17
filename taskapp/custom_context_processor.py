from .models import Category, Question, Answer
from django.views.generic.list import ListView

# class access_all(ListView):
#
#     model = Category
#     model = Answer
#     model = Question
#
#     def get_context_data(self, *, object_list=None, **kwargs,):
#         context = super().get_context_data(**kwargs)
#         context['categories'] = Category.objects.all()
#         context['all_ques'] = Question.objects.all()
#         context[''] = Answer.objects.all()

def access_all(request):
    get_question = Question.objects.all()
    get_answer = Answer.objects.all()
    get_categories = Category.objects.all()
    context ={
        'all_ques': get_question,
        'get_answer': get_answer,
        'categories': get_categories
    }
    return context

