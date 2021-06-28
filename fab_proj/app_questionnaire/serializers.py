from rest_framework import serializers

from app_questionnaire.models import PollModel, QuestionModel, AnswerModel


class AnswerSerializer(serializers.ModelSerializer):
    """Сериализация ответов к вопросам"""
    class Meta:
        model = AnswerModel
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    """Сериализация вопросов"""
    class Meta:
        model = QuestionModel
        fields = '__all__'


class PollSerializer(serializers.ModelSerializer):
    """Сериализация опросов"""
    class Meta:
        model = PollModel
        fields = '__all__'  # ['id', 'title', 'description', 'start_date', 'stop_date', 'choice_answer']
        depth = 1
