from .models import Task
from django.http import JsonResponse
from .serializers import TaskSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])

def index(request):
    if request.method == 'GET':
        task = Task.objects.all()
        serializers = TaskSerializers(task, many=True)
        data = {
            'task': serializers.data
        }

        return Response(data)
    elif request.method == 'POST':
        task = TaskSerializers(data=request.data)
        if task.is_valid():
            task.save()
            return Response(task.data, status=status.HTTP_201_CREATED)
