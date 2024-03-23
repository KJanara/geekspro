from .models import Task
from .serializers import TaskSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class TaskCreate(ListCreateAPIView):
  queryset = Task.objects.all()
  serializer_class = TaskSerializer

class TaskD(RetrieveUpdateDestroyAPIView):
   queryset = Task.objects.all()
   serializer_class = TaskSerializer
   lookup_field = "id"
