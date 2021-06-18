from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from app_questionnaire.views import PollListView, PollDetailView, QuestionList

# router = DefaultRouter()
# router.register('polls', PollViewSet, basename='polls')


urlpatterns = [
    path('polls/', PollListView.as_view(), name='polls_list'),
    path('polls/<int:pk>/', PollDetailView.as_view(), name='polls_detail'),
    path('polls/<int:pk>/questions/', QuestionList.as_view(), name='question_list'),
    # path('polls/<int:pk>/questions/<int:question_pk>/', QuestionList.as_view(
    #     {'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy'}), name='question_change'),
    # path('polls/<int:pk>/questions/<int:question_pk>/answers/', AnswerCreate.as_view(), name='answer_create'),
    # path('answers/<int:pk>/', AnswerList.as_view(), name='answer_list'),
]

urlpatterns += [
    path('auth/', include('rest_framework.urls')),
]

# urlpatterns += router.urls