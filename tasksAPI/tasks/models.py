from django.db import models
from uuid import uuid4

# Create your models here.
class Collections(models.Model):
    id = models.UUIDField(default=uuid4(), primary_key=True)
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=100, blank=True, null=True)
    archived = models.BooleanField(default=False)
    completed = models.IntegerField(default=0)
    total_tasks = models.IntegerField(default=0)

    @property
    def progress(self):
        return (self.completed/self.total_tasks) * 100

    def __str__(self) -> str:
        return self.title.capitalize()

class Tasks(models.Model):
    _id = models.AutoField()
    collection = models.ForeignKey(Collections)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True, null=True)
    completed = models.BooleanField(default=False)

    @property
    def id(self):
        return str(self.collections + self.id)


    def __str__(self) -> str:
        return self.title
