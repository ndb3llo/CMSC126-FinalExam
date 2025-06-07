# models.py
from django.db import models

class HandbookSection(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()