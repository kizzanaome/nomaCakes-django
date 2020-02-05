from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from apps.authentication.api.serializers import (LoginSerializer,
                                                 SignupSerializer)
from apps.authentication.models import User

# Create your views here.

@api_view(['POST',])
def signup_view(request):

    serializer = SignupSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        user = serializer.save()
        data['response'] = 'successfully registered new user.'
        data['email'] = user.email
        data['username'] = user.username
        data['contact'] = user.contact
    else:
        data = serializer.errors

    return Response(data)

@api_view(['POST',])
def login_view(request):

    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        new_data= serializer.data
        new_data['response'] = 'You have succesfully logged in'
        return Response(new_data, status = HTTP_200_OK)
    return Response(serializer.errors, HTTP_400_BAD_REQUEST)
