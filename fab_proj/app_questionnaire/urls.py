from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from app_questionnaire.views import PollListView, PollDetailView, QuestionList, QuestionListView

# router = DefaultRouter()
# router.register('polls', PollListView.as_view(), basename='polls')


urlpatterns = [
    path('polls/', PollListView.as_view(), name='polls_list'),
    path('polls/<int:pk>/', PollDetailView.as_view(), name='polls_detail'),
    path('polls/<int:pk>/questions/', QuestionList.as_view(), name='question_list'),
    path('question/', QuestionListView.as_view(), name='question_list')
    # path('polls/<int:pk>/questions/<int:question_pk>/answers/', AnswerList.as_view(), name='answer_create'),
    # path('answers/<int:pk>/', AnswerList.as_view(), name='answer_list'),
]

urlpatterns += [
    path('auth/', include('rest_framework.urls')),
]

# urlpatterns += router.urls