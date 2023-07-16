from .models import Task , MyUser
from rest_framework import serializers

class TaskSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        id = serializers.ReadOnlyField()
        due_date = serializers.ReadOnlyField()
        model = Task
        fields = ('id','name','description','due_date','created_by_id')
        extra_kwargs = {'created_by_id': {'read_only': True}}

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super().update(instance, validated_data)
        

class myUserSerializers(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    password = serializers.CharField(
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'},
        write_only=True
    )
    class Meta:
        model = MyUser
        fields = ['id','email','name','password','date_of_birth','phone']
    def create(self, validated_data):
        user = MyUser.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
            date_of_birth=validated_data['date_of_birth'],
            phone=validated_data['phone'],
        )
        return user
    

    def update(self, instance, validated_data):
        # Handle updating user account
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super().update(instance, validated_data)