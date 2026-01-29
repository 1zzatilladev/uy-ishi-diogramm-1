from django.urls import path
from .views import AnswerApiVIew,AnswerDetailApiVIew,QuestionApiVIew,QuestionDetailApiVIew,ResultApiVIew,ResultDetailApiVIew,QuizApiVIew,QuizDetailApiVIew

urlpatterns = [
    path('answer/',AnswerApiVIew.as_view()),
    path('result/',ResultApiVIew.as_view()),
    path('question/',QuestionApiVIew.as_view()),
    path('quiz/',QuizApiVIew.as_view()),
    path('question/<int:pk>/', QuestionDetailApiVIew.as_view()),
    path('answer/<int:pk>/', AnswerDetailApiVIew.as_view()),
    path('result/<int:pk>/', ResultDetailApiVIew.as_view()),
    path('result/<int:pk>/', QuizDetailApiVIew.as_view()),
 ]
