from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from rest_framework.views import APIView 
from rest_framework.response import Response
from .models import User,Question,Quiz,Answer,Result
from .serializer import QuestionSarializer,QuizSarializer,AnswerSarializer,ResultSarializer,UserSerializer
from rest_framework.generics import ListAPIView, ListCreateAPIView, CreateAPIView, \
    RetrieveAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView, \
        UpdateAPIView, DestroyAPIView

#---------------------------
class QuizApiVIew(ListCreateAPIView):
    serializer_class = QuizSarializer
    queryset = Quiz.objects.all()


class QuizDetailApiVIew(RetrieveUpdateDestroyAPIView):
    serializer_class = QuizSarializer
    queryset = Quiz.objects.all()

#---------------------------
class QuestionApiVIew(ListCreateAPIView):
    serializer_class = QuestionSarializer
    queryset = Question.objects.all()


class QuestionDetailApiVIew(RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionSarializer
    queryset = Question.objects.all()
#----------------------

class AnswerApiVIew(ListCreateAPIView):
    serializer_class = AnswerSarializer
    queryset = Answer.objects.all()


class AnswerDetailApiVIew(RetrieveUpdateDestroyAPIView):
    serializer_class = AnswerSarializer
    queryset = Answer.objects.all()

#-------------------------
class ResultApiVIew(ListCreateAPIView):
    serializer_class = ResultSarializer
    queryset = Result.objects.all()


class ResultDetailApiVIew(RetrieveUpdateDestroyAPIView):
    serializer_class = ResultSarializer
    queryset = Result.objects.all()

#---------------------------------
class UserApiVIew(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UsertDetailApiVIew(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
