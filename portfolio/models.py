from django.db import models

# Create your models here.
#class Project(models.Model):
#    title=models.CharField(max_length=100)
#    description = models.CharField(max_length=250)
#    image = models.ImageField(upload_to='portfolio/images/',height_field=None, width_field=None)
#    url=models.URLField(blank=True)

class Skill(models.Model):
    title=models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/skills/')
    


    def __str__(self):
        return self.title