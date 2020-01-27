from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)

class UserManager(BaseUserManager):

    def create_user(self, username, telephone, email, password=None):
        """Create and return a `User` with an email, username and password."""
        if username is None:
            raise TypeError('Users must have a username.')

        if telephone is None:
            raise TypeError('Users must have a telephone numnber.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(username=username, telephone=telephone, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, telephone, email, password):
        
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, telephone, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

# Create your models here.
class User(AbstractBaseUser):

    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, null=True)
    telephone = models.CharField(db_index=True, max_length=255, unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # The `USERNAME_FIELD` property tells us which field we will use to log in.
    # In this case, we want that to be the email field.
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    # Tells Django that the UserManager class defined above should manage
    # objects of this type.
    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

