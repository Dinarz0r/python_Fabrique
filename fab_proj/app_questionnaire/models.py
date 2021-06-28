from django.db import models
from rest_framework.exceptions import ValidationError


class PollModel(models.Model):
    """
    Модель опроса:
    """
    title = models.CharField('название', max_length=100)
    description = models.TextField('описание', max_length=1000)
    start_date = models.DateTimeField('дата старта опрос')
    stop_date = models.DateTimeField('дата окончания опроса', )
    question = models.ForeignKey('QuestionModel', related_name='question_poll', on_delete=models.CASCADE,
                                 verbose_name='Опрос')

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

    def __str__(self):
        return self.title


def validateQuestionType(value):
    if not value in ['text', 'choice_one', 'choice_many']:
        raise ValidationError('Invalid question type')


class OptionQuestionModel(models.Model):
    """Модель варианта ответа"""
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text


class QuestionModel(models.Model):
    """Модель вопроса связанного с опросом"""
    TYPE_QUESTION_CHOICE = [
        ('text', 'ответ текстом'),
        ('choice_one', 'ответ с выбором одного варианта'),
        ('choice_many', 'ответ с выбором нескольких вариантов'),
    ]
    poll = models.ForeignKey(PollModel, related_name='questions', on_delete=models.CASCADE, verbose_name='Опрос')
    text_question = models.TextField('текст вопроса', max_length=100)
    type_question = models.CharField('тип опроса', max_length=11, choices=TYPE_QUESTION_CHOICE)

    # option_question = models.ManyToManyField(OptionQuestionModel, verbose_name='варианты ответов', blank=True,
    #                                          null=True)

    @property
    def hasOptionType(self):
        """Геттер получения типа вопроса"""
        return self.type_question

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.text_question


class AnswerModel(models.Model):
    """Модель ответа на вопрос"""
    question = models.ForeignKey(QuestionModel, related_name='answers', on_delete=models.CASCADE)
    answerText = models.CharField('текст ответа', max_length=300, blank=True, null=True)
    option_question = models.ManyToManyField(OptionQuestionModel, verbose_name='варианты ответов', blank=True,
                                             related_name='question_model')
    many_option = models.ForeignKey(OptionQuestionModel, on_delete=models.CASCADE, blank=True, null=True,
                                    verbose_name='выбор одного')

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return f'Ответ на вопрос: {self.question}'
