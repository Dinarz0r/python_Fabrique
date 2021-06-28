from django.contrib import admin

from app_questionnaire.models import PollModel, AnswerModel, QuestionModel, OptionQuestionModel

admin.site.register(PollModel)
admin.site.register(AnswerModel)
admin.site.register(QuestionModel)
admin.site.register(OptionQuestionModel)
