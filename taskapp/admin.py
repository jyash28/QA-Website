from django.contrib import admin
from .models import User, Question, Answer, Category


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'firstname', 'lastname', 'is_staff', 'is_active', 'is_superuser', 'created', 'modified'
                    )
    list_filter = ('admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'image')}),
        ('Permissions', {'fields': ('admin',)}),

    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'name', 'created', 'modified')
    list_filter = ('title',)

    ordering = ('title',)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('name', 'question_id','created', 'modified')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass



