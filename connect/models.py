from django.db import models

# Create your models here.
class Connect(models.Model):
    
    image = models.ImageField(upload_to='portfolio/images/connect/')
    url=models.URLField(blank=True)

    