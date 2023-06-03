from .models import Task
from django.http import JsonResponse
from .serializers import TaskSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])

def index(request):
    if request.method == 'GET':
        task = Task.objects.all().order_by('-id')
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

@api_view(['GET','PUT','DELETE'])

def detail(request,id):
    
    try:
        task = Task.objects.get(pk=id)
        
    except Task.DoesNotExist :
        return Response(status=status.HTTP_404_NOT_FOUND)
        # handle get request
    if request.method == 'GET':
        serializers = TaskSerializers(task)
        return Response(serializers.data)
        # handle update request
    elif request.method == 'PUT':
        ModifyTask = TaskSerializers(task, data=request.data)
        if ModifyTask.is_valid(): 
            ModifyTask.save()
            return Response(ModifyTask.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

