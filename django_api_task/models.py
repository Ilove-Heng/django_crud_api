from django.db import models
# from django.utils import timezone
from datetime import date

class Task(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField()
    due_date=models.DateField(default=date.today)

    def __str__(self) -> str:
        return "Task: " + self.name

    class Meta:
        db_table='task'
