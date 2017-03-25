from rest_framework import serializers
from .models import ToDoList


class ToDoListSerializer(serializers.ModelSerializer):

    """ To map the Model instance into JSON"""

    class Meta:
        model = ToDoList
        fields = ('id', 'name', 'description', 'deadline', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')

