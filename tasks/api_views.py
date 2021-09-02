from rest_framework import response
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend

from tasks.serializers import TaskSerializer
from tasks.models import Task

class TaskList(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id',)

class TaskCreate(CreateAPIView):
    serializer_class = TaskSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class TaskRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    lookup_field = 'id'
    serializer_class = TaskSerializer

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

