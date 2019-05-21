from django.db import models
from datetime import datetime
# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=1000)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    media = models.ImageField(upload_to='media',blank=True)
    def __str__(self):
        return self.title