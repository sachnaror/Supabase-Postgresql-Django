# Create your models here.
from django.db import models

# Create your models here.


class Todo(models.Model):
    label = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.label}"
