from django import template
from taskapp.models import Question, Category, User
from django.db.models import Count

register = template.Library()

def most_ans(ques):
    # most_answers = Question.objects.annotate(Count('answer')).filter(answer__gt=2)
    most_answers = ques.annotate(answer_count=Count('answer')).filter(answer_count__gt=1)
    return most_answers

def top_ques(question):
    top_question = Question.objects.all().order_by('created').reverse()[:4]
    return top_question

# def related_quest(question):
#     related_question = Question.objects.filter(question_type_id=question.id).exclude()
#     return related_question

def top_mem(member):
    top_members = User.objects.annotate(question_count=Count('User')).filter(question_count__gt=1)
    return top_members

@register.simple_tag
def cate_question(cat, ques):
    category_question = Question.objects.filter(question_type_id=cat)
    return category_question



# register.filter('cate_question' , cate_question)

register.filter('most_ans', most_ans)

register.filter('top_ques', top_ques)

register.filter('top_mem', top_mem)

