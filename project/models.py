from django.db import models

# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=100)
    date=models.DateField()
    description=models.CharField(max_length=4000)
    url=models.URLField()

    def __str__(self):
        return self.title