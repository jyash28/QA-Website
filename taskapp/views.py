from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from taskapp.forms import ContactForm, QuestionForm, AnswerForm
from django.views import generic
from django.views.generic.base import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.core.exceptions import ValidationError
from taskapp.models import Question, Category, User, Answer
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User, auth

from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.

class IndexView(ListView):
    template_name = 'index.html'
    model = Question
    queryset = Question.objects.all()
    paginate_by = 2


    def get_context_data(self, *, object_list=None, **kwargs,):
        context = super().get_context_data(**kwargs)
        # context['categories'] = Category.objects.all()
        # context['all_ques'] = Question.objects.all()
        # context['user'] = User.objects.all()
        # context['quest'] = Question.objects.filter()
        context['user'] = self.request.user
        return context

# def index(request):
#     contact_list = Question.objects.all()
#     paginator = Paginator(contact_list, 2) # Show 25 contacts per page.
#
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'index.html', {'page_obj': page_obj})



class QuestionView(generic.CreateView):
    template_name = "index.html"
    form_class = QuestionForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
        else:
            return render(request, self.template_name, {'form': form})
        return redirect('taskapp:index')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['all_ques'] = Question.objects.all()
    #     return context
        # context = super().get_context_data(**kwargs)
        # context['categories'] = Category.objects.all()
        # context['user'] = User.objects.all()
        # return context

class AnswerView(generic.CreateView):
    template_name = "index.html"
    form_class = AnswerForm


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # form = form.save(commit=False)
            form.save()
        else:
            return render(request, self.template_name, {'form': form})
        return redirect('taskapp:index')





class SignUpView(generic.CreateView):
    form_class = ContactForm
    template_name = 'header.html'
    success_url = reverse_lazy('taskapp:login')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid(request):
            # Email = form.cleaned_data.get('email')
            # password1 = form.cleaned_data.get('password')
            # password2 = form.cleaned_data.get('password2')
            # if User.objects.filter(email=Email).exists():
            #     messages.info(request, 'email taken')
            # if password1 != password2:
            #     # raise ValidationError("Passwords don't match")
            #     messages.info(request,"password did not match")
            #     # return redirect('taskapp:index')
            # subject = 'welcome to GFG world'
            # message = f"Hi {form.cleaned_data.get('email')}, thank you for registering in this website."
            # email_from = settings.EMAIL_HOST_USER
            # recipient_list = [form.cleaned_data.get('email'), ]
            # send_mail(subject, message, email_from, recipient_list)
            form.save()
        return redirect('taskapp:index')

class LoginView(generic.View):

    # def get(self, request):
    #     return redirect('taskapp:index')

    def post(self, request):
        data = request.POST
        email = data.get('email', None)
        password = request.POST['password']

        user = authenticate(email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('taskapp:index')
        # else:
        messages.info(request, "invalid credentials")
            # return redirect(reverse_lazy("taskapp:login"))
        return redirect('taskapp:index')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('taskapp:index')


class QuestionDetailView(DetailView):
    model = Question
    template_name = 'question_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class QuestionCategoryView(ListView):
    model = Question
    template_name ='question_categories.html'
    queryset = Question.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post']= Question.objects.filter(question_type_id=self.kwargs['pk'])
        context['cat_id']= self.kwargs['pk']
        return context