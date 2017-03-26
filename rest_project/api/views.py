from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .serializer import ToDoListSerializer
from .models import ToDoList


class CreateView(generics.ListCreateAPIView):

    """ Class to define the behaviour REST Api"""

    queryset = ToDoList.objects.all()
    serializer_class = ToDoListSerializer

    def perform_create(self, serializer):

        """ Save the post data when creating a new todolist """

        serializer.save()

