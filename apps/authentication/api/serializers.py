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
        user = User(email = self.validated_data['email'], username = self.validated_data['username'], contact = self.validated_data['contact'])
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match'})

        user.set_password(password)
        user.save()

        return user
