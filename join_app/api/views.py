from rest_framework.decorators import api_view
from .serializers import CategorySerializer, NamesSerializer, TaskstatusSerializer, PrioritySerializer, TasksSerializer
from join_app.models import Category, Names, TaskStatus, Priority, Tasks
from rest_framework.response import Response
from rest_framework import viewsets


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class NamesViewSet(viewsets.ModelViewSet):
    queryset = Names.objects.all()
    serializer_class = NamesSerializer


class TaskstatusViewSet(viewsets.ModelViewSet):
    queryset = TaskStatus.objects.all()
    serializer_class = TaskstatusSerializer

    def get_tasks_with_status_names():
        tasks = Tasks.objects.prefetch_related('status').all()

        task_list = []
        for task in tasks:
            task_list.append({
                'status': [status.name for status in task.status.all()],
            })

        return task_list


class PriorityViewSet(viewsets.ModelViewSet):
    queryset = Priority.objects.all()
    serializer_class = PrioritySerializer


class TasksViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
