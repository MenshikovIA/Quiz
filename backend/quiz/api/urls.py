from django.urls import path, include
from .views import AnswerCreateAPIView, QuizViewSet, QuestionAPIView, UserAnswers
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"quiz", QuizViewSet)


urlpatterns = [
    # path('', router.urls),
    path('quiz_questions/<int:pk>/', QuestionAPIView.as_view(), name='quiz'),
    path('answer/', AnswerCreateAPIView.as_view(), name='answer'),
    path('answers/<int:pk>/', UserAnswers.as_view(), name='user-answers')
] + router.urls

