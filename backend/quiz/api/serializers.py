from rest_framework import serializers

from ..models import Quiz, Question, Answer


class QuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quiz
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = "__all__"


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = "__all__"


class UserAnswersListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = "__all__"

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
