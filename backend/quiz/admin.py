from django.contrib import admin
from .models import Question, Quiz, Answer


class QuizAdmin(admin.ModelAdmin):
    @staticmethod
    def get_readonly_fields(request, obj=None):
        if obj:
            return ["start_date", ]
        else:
            return []


class QuestionAdmin(admin.ModelAdmin):
    list_filter = ('quiz', )


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
