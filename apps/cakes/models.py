from django.db import models
from taggit.managers import TaggableManager
from apps.authentication.models import User


class Cake(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=300)
    price = models.IntegerField()
    rating = models .IntegerField(null=True)
    category = models.CharField(max_length=255)
    tags = TaggableManager(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_tags_display(self):
        return self.tags.values_list('name', flat=True)
