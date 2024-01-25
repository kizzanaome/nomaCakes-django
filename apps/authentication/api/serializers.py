from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError
from rest_framework import serializers
from django.shortcuts import get_object_or_404

from ..models import User
from .utils import validate_username, validate_password, validate_email, validate_contact
from django.db import IntegrityError


def find_email_by_username(username):
    try:
        user_object = User.objects.get(
            username=username.strip().lower())
        return user_object.email
    except User.DoesNotExist:
        raise serializers.ValidationError(
            'A user with this username and password was not found.'
            )

class SignupSerializer(serializers.ModelSerializer):

    email = serializers.EmailField()
    username = serializers.CharField()
    contact = serializers.CharField()

    class Meta:
        model = User
        fields = ['email', 'username', 'contact', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True
            },
            
        }

    def validate_username(self, username):
        return validate_username(username)

    def validate_password(self, password):
        return validate_password(password)

    def validate_email(self, email):
        return validate_email(email)

    def validate_contact(self, contact):
        return validate_contact(contact)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):

    # serializer to map the login model instance into JSON format.

    # email = serializers.EmailField()
    # password = serializers.CharField(write_only=True)
    username = serializers.CharField(max_length=255, required=False)
    email = serializers.CharField(max_length=255, required=False)
    password = serializers.CharField(max_length=128, write_only=True)
    # token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        """ meta class to map the serializer fields to the model field"""

        model = User
        fields = ['username', 'email', 'password']

    def validate(self, data):
        username = data.get('username', None)
        email = data.get('email', None)
        password = data.get('password', None)

        # email = request.data.get('email')
        #hash the password
        # hash_password = User.set_password(password)
        # valid_password = User.check_password(password, hash_password)
        # check_user = User.objects.get(email=email, password=password)
        # print(check_user)
        # print("check_user")
        # exit()

        # if username is not None:
        #     print(username)
        email = find_email_by_username(username)
        user = authenticate(username=email, password=password)
        print(user)
        if user is None:
            raise ValidationError("Incorrect credentials please try again")
        return {
            'email': user.email
        }
