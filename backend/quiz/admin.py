from django.contrib import admin
from django import forms
from .models import Question, Quiz, Answer, QuestionOption


class QuizAdmin(admin.ModelAdmin):
    @staticmethod
    def get_readonly_fields(request, obj=None):
        if obj:
            return ["start_date", ]
        else:
            return []


class QuestionAdmin(admin.ModelAdmin):
    list_filter = ('quiz', )


class CustomModelForm(forms.ModelForm):
    class Meta:
        model = QuestionOption
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CustomModelForm, self).__init__(*args, **kwargs)
        self.fields['question'].queryset = Question.objects.filter(type__contains='option')


class QOptionAdmin(admin.ModelAdmin):
    form = CustomModelForm


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionOption, QOptionAdmin)
admin.site.register(Answer)
