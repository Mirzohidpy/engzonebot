from django.contrib import admin
from .models import User, Teacher, Level, ExistingStudent, TrialVideos, Answer, Question, LessonOrder

# Register your models here.


admin.site.register(User)
admin.site.register(Teacher)
admin.site.register(Level)
admin.site.register(ExistingStudent)
admin.site.register(TrialVideos)
admin.site.register(LessonOrder)


class AnswerInlineModel(admin.TabularInline):
    model = Answer
    fields = [
        'answer',
        'is_correct',
    ]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'points',
        'level',
        'open_period'
    ]
    list_display = [
        'title',
        'updated_at'
    ]
    inlines = [
        AnswerInlineModel,
    ]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'answer',
        'is_correct',
        'question'
    ]
