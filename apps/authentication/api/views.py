from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.authentication.api.serializers import SignupSerializer

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
