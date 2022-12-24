from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Collections, Tasks
from .serializers import CollectionSerializer, TaskSerializer
from rest_framework.response import Response
from rest_framework import status
from Users.exceptions import UserNotFound, CollectionNotFound
from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

# Create your views here.

# we will first create a collection
class CollectionViewSet(ModelViewSet):
    queryset = Collections.objects.all()
    serializer_class = CollectionSerializer
    
    def get_permissions(self):
        if self.action != "list":
            permission_classes = [permissions.IsAuthenticated, IsOwner]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        # let create a new collection
        serializer = CollectionSerializer(data=request.data)
        if serializer.is_valid():
            # here we assign the current user to the owner of the collection
            try:
                serializer.validated_data["owner"] = request.user
                collection = serializer.save()
            except:
                raise UserNotFound
        else:
            return Response({"detail":"Invalid entries made"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(CollectionSerializer(instance=collection).data)

class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Tasks.objects.all()
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            task = serializer.save()
            return Response(TaskSerializer(instance=task).data)
        else:
            return Response({"status":"Creation failed"})
