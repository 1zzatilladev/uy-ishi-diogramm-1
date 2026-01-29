from rest_framework.serializers import ModelSerializer
from .models import User,Question,Quiz,Answer,Result
class UserSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = User
class QuestionSarializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Question

class QuizSarializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Quiz
class AnswerSarializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Answer

class ResultSarializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Result