from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
# from taggit.managers import TaggableManager
from users.models import User


class Cake(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=300)
    price = models.IntegerField()
    rating = models .IntegerField(null=True)
    category = models.CharField(max_length=255)
    # tags = TaggableManager(blank=True)
    created_at = models.DateTimeField(verbose_name='date created', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='updated at', auto_now=True)
    # created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    # def get_tags_display(self):
    #     return self.tags.values_list('name', flat=True)
