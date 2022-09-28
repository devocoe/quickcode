from operator import mod
from pyexpat import model
from turtle import title
from django.db import models
import uuid

# Create your models here.


class Language(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          null=False, blank=False, editable=False)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Code(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          null=False, blank=False, editable=False)
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=100, unique=True)
    code = models.TextField(max_length=1000)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
