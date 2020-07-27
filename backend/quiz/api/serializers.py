from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from ..models import Quiz, Question, Answer, QuestionOption


class QuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quiz
        exclude = ('id', )


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        exclude = ('id', )


class QuestionOptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionOption
        exclude = ('id', )


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = "__all__"

    def validate_options(self, options):
        data = self.get_initial()
        question_id = data.get("question")
        question = Question.objects.get(id=question_id)
        text = data.get("text")

        if question.type == 'text':
            if not text:
                raise ValidationError("This question requires a text answer")
            elif options:
                raise ValidationError("This question requires only a text answer")

        elif question.type == 'one_option':
            if text:
                raise ValidationError("No text answer is allowed to this question")
            elif len(options) != 1:
                raise ValidationError("Only one option is allowed to this question")

        elif question.type == 'several_options':
            if text:
                raise ValidationError("No text answer is allowed to this question")
            elif not options:
                raise ValidationError("You should pick at least one option")

        for option in options:
            if option.question != question:
                raise ValidationError("One of the options does not belong to this question")

        return options


class UserAnswersListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        exclude = ('id', )

    question_text = serializers.SerializerMethodField()
    question_type = serializers.SerializerMethodField()
    quiz_title = serializers.SerializerMethodField()

    @staticmethod
    def get_question_text(instance):
        return instance.question.text

    @staticmethod
    def get_question_type(instance):
        return instance.question.type

    @staticmethod
    def get_quiz_title(instance):
        return instance.question.quiz.title
