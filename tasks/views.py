from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framweork.response import APIView
from .models import Task
from .serializers import TaskSerializer
from drf_api.permission import IsOwnerOrReadOnly

class TaskList(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    
    def get(self,request):
        tasks = Task.objects.filter(user=request.user)
        serializer = TaskSerializer(
            tasks, many=True, context={'request' : request}
        )
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TaskSerializer(
            data=rquest.data, context={'request' : request}
        )
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(Serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDetail(APIView):
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            # Fetch the task and ensure it's owned by the authenticated user
            task = Task.objects.get(pk=pk, user=self.request.user)
            self.check_object_permissions(self.request, task)
            return task
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        # Retrieve a single task
        task = self.get_object(pk)
        serializer = TaskSerializer(
            task, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        # Update a specific task
        task = self.get_object(pk)
        serializer = TaskSerializer(
            task, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Delete a specific task
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)