from django.db import models
from uuid import uuid4
from django.conf import settings

# Create your models here.
class Collections(models.Model):
    class Meta:
        verbose_name = "Collection"


    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid4(), primary_key=True)
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=100, blank=True, null=True)
    archived = models.BooleanField(default=False)
    completed = models.IntegerField(default=0)
    total = models.IntegerField(default=0)

    @property
    def progress(self):
        return (self.completed/self.total) * 100

    def __str__(self) -> str:
        return self.title.capitalize()

class Tasks(models.Model):
    class Meta:
        verbose_name = "Task"
    collection = models.ForeignKey(Collections, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    reminder = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    completed = models.BooleanField(default=False)


    def __str__(self) -> str:
        return self.title.capitalize()
