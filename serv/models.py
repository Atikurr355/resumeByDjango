from django.db import models

# Create your models here.

class Service(models.Model):
    logo = models.ImageField(upload_to="logos")
    title = models.CharField(max_length=60)
    content = models.TextField()

    def __str__(self):
        return self.title
    