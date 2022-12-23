from rest_framework import serializers
from . models import Collections, Tasks

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collections
        exclude = ["owner"]
        read_only_fields = ["id", "total", "completed"]


class TaskSerializer(serializers.ModelSerializer):
    collectionId = serializers.CharField(required=False)
    class Meta:
        model = Tasks
        fields = "__all__"
        # ["title", "description"]
