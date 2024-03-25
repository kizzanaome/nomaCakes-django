from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from rest_framework import serializers
from django.shortcuts import get_object_or_404

from .models import User
from .utils import validate_username, validate_password, validate_email, validate_contact
from django.db import IntegrityError


class SignupSerializer(serializers.ModelSerializer):

    id= serializers.IntegerField(read_only=True)
    email = serializers.EmailField()
    username = serializers.CharField()
    contact = serializers.CharField()

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'contact', 'password']
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

    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    class Meta:
        """ meta class to map the serializer fields to the model field"""

        model = User
        fields = ['email', 'password']

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)
        user = authenticate(username=email, password=password)
        if user is None:
            raise ValidationError("Incorrect credentials please try again")
        return {
            'email': user.email
        }
