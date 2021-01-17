from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)
    blog_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name
