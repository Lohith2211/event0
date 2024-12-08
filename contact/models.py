from django.db import models

class EventContact(models.Model):
    event_name = models.CharField(max_length=100)
    organizer_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    query = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.event_name} by {self.organizer_name}"


# Create your models here.
