from django.db import models

# Create your models here.
class Authors(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, db_index=True, unique=True)
    picture = models.CharField(max_length=256)


class Articles(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.IntegerField(db_index=True)
    category = models.SlugField(max_length=64, db_index=True)
    title = models.CharField(max_length=64)
    summary = models.CharField(max_length=128)
    firstParagraph = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
