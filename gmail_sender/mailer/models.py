from django.db import models

# Create your models here.
# gmail_sender/models.py

from django.db import models

class EmailDetail(models.Model):
    to_email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
