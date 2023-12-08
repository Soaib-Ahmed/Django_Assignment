from django.db import models


# Create your models here.
class Task(models.Model):
    taskTitle = models.CharField(max_length=255)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    taskAssignDate = models.DateField()
    categories = models.ManyToManyField('category.TaskCategory', blank=True)

    def __str__(self):
        return self.taskTitle