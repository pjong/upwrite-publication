from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

SECTION_CHOICES = [

    ('regional', 'Regional'),
    ('national', 'National'),
    ('editorial', 'Editorial'),
    ('provincial', 'Provincial'),
    ('legal', 'Legal'),
]

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()  # rich text editor
    section = models.CharField(max_length=20, choices=SECTION_CHOICES)
    image = models.ImageField(upload_to='articles/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

