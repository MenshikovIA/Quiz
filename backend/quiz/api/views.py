from rest_framework import viewsets, generics

from .serializers import QuizSerializer, QuestionSerializer, AnswerSerializer, UserAnswersListSerializer
from ..models import Quiz, Question, Answer


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all().order_by('-start_date')
    serializer_class = QuizSerializer


class QuestionAPIView(generics.ListAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Question.objects.filter(quiz__id=pk)


class AnswerCreateAPIView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class UserAnswers(generics.ListAPIView):
    serializer_class = UserAnswersListSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Answer.objects.filter(user_id=pk)
