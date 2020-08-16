from django.db import models

# Create your models here.
class Node(models.Model):
    floor_name = models.CharField(max_length=20)
    light1_name = models.CharField(max_length=20)
    light1_status = models.CharField(max_length=20)
    light2_name = models.CharField(max_length=20)
    light2_status = models.CharField(max_length=20)

    def __str__(self):
        return self.floor_name
