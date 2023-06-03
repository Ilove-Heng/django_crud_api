from rest_framework import serializers
from .models import Task

class TaskSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        id = serializers.ReadOnlyField()
        due_date = serializers.ReadOnlyField()
        model = Task
        fields = ('id','name','description','due_date')