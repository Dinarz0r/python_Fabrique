from datetime import datetime
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin, ListModelMixin, \
    CreateModelMixin
from rest_framework import permissions
from rest_framework.response import Response

from app_questionnaire.models import PollModel, QuestionModel
from app_questionnaire.serializers import PollSerializer, QuestionSerializer


class PollListView(ListModelMixin, CreateModelMixin, GenericAPIView):
    """Представление для получения списка опросов и вопросов в ней
    а так же не для авторизованного пользователя он будет выводить только действующие опросы"""
    serializer_class = PollSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        if self.request.successful_authenticator:
            queryset = PollModel.objects.all()
        else:
            queryset = PollModel.objects.filter(stop_date__gt=datetime.today())
        return queryset

    def get(self, request):
        # test_query = PollModel.objects.all().first()
        # print(list(test_query.questions.all().first().poll.choice_answer.all()))
        return self.list(request)

    def post(self, request):
        return self.create(request)


class PollDetailView(UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericAPIView):
    """Представление для получения детальной информации о скидке, а так же для его редактирования"""

    queryset = PollModel.objects.all()
    serializer_class = PollSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        req_date = str(datetime.fromisoformat(request.data['start_date']))
        check_date = str(PollModel.objects.filter(id=kwargs['pk']).first().start_date)[:19]
        if req_date != check_date:
            raise PermissionDenied(detail='Нельзя менять дату старта опроса', code=403)
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        # if not request.user.has_perm('права на удаление'):
        #     print('У вас нет прав')
        #     raise PermissionDenied(detail='У вас нет прав', code=403)
        return self.destroy(request, *args, **kwargs)


class QuestionList(UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = QuestionSerializer
    queryset = QuestionModel.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        # if not request.user.has_perm('права на удаление'):
        #     print('У вас нет прав')
        #     raise PermissionDenied(detail='У вас нет прав', code=403)
        return self.destroy(request, *args, **kwargs)


class QuestionListView(ListModelMixin, CreateModelMixin, GenericAPIView):
    """Представление для получения списка вопросов в ней
    а так же не для авторизованного пользователя он будет выводить только действующие опросы"""
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        if self.request.successful_authenticator:
            queryset = QuestionModel.objects.all()
        else:
            queryset = QuestionModel.objects.filter(stop_date__gt=datetime.today())
        return queryset

    def get(self, request):
        """тут может добавить фильтр для вывода списка вопрос напрмер по дате старт энд опроса"""
        return self.list(request)

    def post(self, request):
        return self.create(request)
