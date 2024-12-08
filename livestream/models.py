from django.db import models
from django.contrib.auth.models import User

class LiveStream(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    stream_url = models.URLField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_live = models.BooleanField(default=False)

    def __str__(self):
        return self.title


# Create your models here.
