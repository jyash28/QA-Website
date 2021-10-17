from django import forms
from taskapp.models import User, Question, Answer
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail


class ContactForm(forms.ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('email', 'firstname', 'lastname', 'password', 'password2', 'image')

    def is_valid(self, request):
        Email = self.data['email']
        password1 = self.data['password']
        password2 = self.data['password2']
        if User.objects.filter(email=Email).exists():
            return messages.error(request, 'email taken')
        if password1 != password2:
            # raise ValidationError("Passwords don't match")
            messages.info(request, "password did not match")
            # return redirect('taskapp:index')
        subject = 'welcome to GFG world'
        message = f"Hi {self.data['email']}, thank you for registering in this website."
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [self.data['email'], ]
        send_mail(subject, message, email_from, recipient_list)
        return Email

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = '__all__'


class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = '__all__'





















