from django.db import models
from categories.models import Category
from datetime import datetime


class Blog(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    image1 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    blog_created = models.DateTimeField(default=datetime.now, blank=True)
    featured = models.BooleanField(default=False)
    mvp = models.BooleanField(default=False)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
