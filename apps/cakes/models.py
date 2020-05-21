from django.db import models
from taggit.managers import TaggableManager


class Cakes(models.Model):
    name = models.CharField(max_length =255)
    description = models.TextField()
    price = models.IntegerField()
    rating = models .IntegerField()
    category = models.CharField(max_length =255)
    tags = TaggableManager()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name