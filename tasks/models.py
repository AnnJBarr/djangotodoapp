from django.db import models

# Create your models here.

class Task(models.Model):
    task_text = models.CharField(max_length=1000)
    created_date = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField()
    complete = models.BooleanField()

    def __str__(self):
        return self.task_text

