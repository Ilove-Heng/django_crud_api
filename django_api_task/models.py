from django.db import models
from django.utils import timezone

class Task(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField()
    due_date=models.DateField(default=timezone.now)

    def __str__(self) -> str:
        return "Task: " + self.name

    class Meta:
        db_table='task'
