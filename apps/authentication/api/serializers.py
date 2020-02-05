from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from rest_framework import serializers

from ..models import User


class SignupSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(
        max_length=17,
        min_length=7,
        write_only=True
    )
    email = serializers.EmailField()
    username = serializers.CharField()
    contact = serializers.CharField()

    class Meta:
        model = User
        fields = ['email', 'username', 'contact', 'password', 'password2']
        extra_kwargs = {
            'password': {
                'write_only': True
            },
        }

    def create(self, validated_data):
        user = User(email=self.validated_data['email'],
                    username=self.validated_data['username'], contact=self.validated_data['contact'])
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError(
                {'password': 'Passwords must match'})

        user.set_password(password)
        user.save()

        return user


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
        password = data.get('password',None)
        user = authenticate(username=email,password=password)
        if user is None:
                raise ValidationError("Incorrect credentials please try again")
        return {
            'email': user.email
        }
