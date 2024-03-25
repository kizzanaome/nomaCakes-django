from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, username,email,contact, password=None):
        
        if username is None:
            raise TypeError('Users must have a username.')

        if contact is None:
            raise TypeError('Users must have a phone number.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(
            username = username,
            contact = contact,
            email = self.normalize_email(email)
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, contact, email, password):
        
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(
            username = username,
            contact = contact,
            email = self.normalize_email(email),
            password = password
        )
        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True
        user.save()

        return user

# Create your models here.
class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(db_index=True, max_length=25)
    email = models.EmailField(db_index=True, verbose_name="email", unique=True)
    contact = models.CharField(db_index=True, max_length=255, unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='last login', auto_now=True)
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

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True
