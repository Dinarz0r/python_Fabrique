from django.db import models


class OneQuestion(models.Model):
    """Выбор одного"""
    text = models.CharField('Выбор', max_length=1000)

    def __str__(self):
        return self.text


class PollModel(models.Model):
    """
    Модель опроса:
    """

    title = models.CharField('название', max_length=100)
    description = models.TextField('описание', max_length=1000)
    start_date = models.DateTimeField('дата старта опрос')
    stop_date = models.DateTimeField('дата окончания опроса', )

    choice_answer = models.ManyToManyField(OneQuestion, verbose_name='варианты ответов', related_name='poll')

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

    def __str__(self):
        return self.title


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

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.text_question




class AnswerModel(models.Model):
    question = models.ForeignKey(QuestionModel, related_name='answers', on_delete=models.CASCADE)
    poll = models.ForeignKey(PollModel, on_delete=models.CASCADE)
    answered_by = models.IntegerField()
    answer_text = models.TextField()
    answer_choice = models.ManyToManyField()
    class Meta:
        unique_together = ("poll", "question", "answered_by")
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return f'Ответ опроса: {self.poll}. Вопроса: {self.question}'
