from django.db import models

# Create your models here.

class Todo_content(models.Model):
    Todo_title = models.CharField(max_length=50)
    Todo_description = models.CharField(max_length=100)
    Todo_status = models.BooleanField(default=False)

    def __str__(self):
        return self.Todo_title
    