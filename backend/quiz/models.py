from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Quiz(models.Model):
    title = models.CharField(max_length=128)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField(blank=True, null=True)

    TYPE_CHOICES = [('text', 'Текст'), ('one_option', 'Один вариант'), ('several_options', 'Несколько вариантов')]
    type = models.CharField(max_length=16, choices=TYPE_CHOICES, default='text')

    def __str__(self):
        return self.text[:150]


class QuestionOption(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    text = models.CharField(max_length=128)

    def __str__(self):
        return self.text


class Answer(models.Model):
    class Meta:
        unique_together = [['question', 'user_id']]

    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    user_id = models.PositiveSmallIntegerField()
    text = models.TextField(blank=True, null=True)
    options = models.ManyToManyField(QuestionOption, blank=True)

    def __str__(self):
        if self.text:
            return self.text[:150]
        else:
            return str(self.id)
