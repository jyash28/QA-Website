from django.urls import path
from . import views
from taskapp.views import SignUpView, LoginView, LogoutView, QuestionView, AnswerView, IndexView, QuestionDetailView, QuestionCategoryView

app_name = 'taskapp'
urlpatterns= [
    path('', IndexView.as_view(), name='index'),

    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    # path('register', views.register, name="register"),
    path('add-question/', QuestionView.as_view(), name="question_create"),
    path('add-answer/', AnswerView.as_view(), name="answer_create"),
    path("register/", SignUpView.as_view(), name='signup'),
    path('detail/<int:pk>/', QuestionDetailView.as_view(), name="detail_question"),
    path('question_categories/<int:pk>', QuestionCategoryView.as_view(), name='question_category'),

]