from .models import Task, MyUser
from django.http import JsonResponse,Http404
from .serializers import TaskSerializers,myUserSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status,viewsets
from rest_framework.authentication import TokenAuthentication
from .permissions import CheckOwnProfile,CheckOwnTask
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

class TaskApiView(APIView):
    # Fetch all tasks
    def get(self,request):
        # task = Task.objects.all().order_by('-id')
        task = Task.objects.all().order_by('-id')[:5]
        serializers = TaskSerializers(task, many=True)
        return Response(serializers.data)

    def post(self,request):
        task = TaskSerializers(data=request.data)
        if task.is_valid():
            task.save()
            return Response(task.data, status=status.HTTP_201_CREATED)
        else: return Response({"message": 'Invalid data'},status=status.HTTP_400_BAD_REQUEST)

     
class TaskDetailApiView(APIView):
    def get_detail(self,request,id=None):
        try:
            task = Task.objects.get(pk=id)
            return task;
        except Task.DoesNotExist :
            raise Http404;


    def get(self,request, id=None):
        task = self.get_detail(request,id);
        serializer = TaskSerializers(task)
        return Response(serializer.data)
    
    def put(self,request,id=None): 
        task = self.get_detail(request,id);
        serializer = TaskSerializers(task,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Task updated successfully 💪"})
        else: return Response({"message": "Invalid task"}, status=status.HTTP_400_BAD_REQUEST)


class TaskViewSet(viewsets.ModelViewSet):
        def get_queryset(self):
            return Task.objects.all().order_by('-id')
        serializer_class  = TaskSerializers
        
        def perform_create(self,serializer):
            serializer.save(created_by=self.request.user)

        def partial_update(self, request, *args, **kwargs):
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)

        def destroy(self, request, *args, **kwargs):
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({"message": "Task deleted successfully"}, status=status.HTTP_200_OK)
        
        def perform_destroy(self, instance):
            instance.delete()


        authentication_classes = [TokenAuthentication]
        permission_classes = [CheckOwnTask]



class LoginApi(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class myuserviewset(viewsets.ModelViewSet):
        serializer_class = myUserSerializers
        def get_queryset(self):
            return MyUser.objects.all()
        
        authentication_classes = [TokenAuthentication]
        # permission_classes = [IsAuthenticated,CheckOwnProfile]
        permission_classes = [CheckOwnProfile]



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
    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



    

