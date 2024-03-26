from django.conf import settings
from django.contrib.auth import login
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from django.http import HttpResponse
from django.utils.html import strip_tags

from .serializers import (LoginSerializer,
                                                 SignupSerializer)
from .models import User

from .tokens import account_activation_token
import uuid
import os

# Create your views here.

@api_view(['POST',])
def signup_view(request):

    serializer = SignupSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        user = serializer.save()

        user.is_active = False
        user.save()
        current_site = get_current_site(request)

        # sending a templated email
        mail_subject ='Activate your account'
        welcome_message = "Welcome " + user.username + ", to NomaCakes!"
        # link_app = "http://localhost:8000"
        context = {
            'user': user,           
            'domain': current_site.domain,
            'uuid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token' : account_activation_token.make_token(user),
            "welcome_message": welcome_message, 
            "link_app": current_site
        }
            
        # print(my_recipient)
        html_message = render_to_string("account_activate.html", context=context)
        plain_message = strip_tags(html_message)
        email_message = EmailMultiAlternatives(
            subject = mail_subject, 
            body = plain_message,
            from_email = os.environ.get('EMAIL_HOST_USER') ,
            to = [user.email]
        )
        email_message.attach_alternative(html_message, "text/html")
        email_message.send()

        # sending a non-templated email
        # message = render_to_string('account_activate.html', {
        #     'user': user,           
        #     'domain': current_site.domain,
        #     'uuid': urlsafe_base64_encode(force_bytes(user.pk)),
        #     'token' : account_activation_token.make_token(user)})
        # email = EmailMessage(mail_subject, message, os.environ.get('EMAIL_HOST_USER'), to=[user.email])
        # email.send()

        # saving data and returning an object
        data['response'] = 'You have successfully registered your account.'\
            ' Please confirm your email address to complete your registration.'
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

@api_view(['GET'])
def activate(request, uuid, token):

    try:
        uuid = force_str(urlsafe_base64_decode(uuid))
        user = User.objects.get(pk=uuid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user,token):
        user.is_active = True
        user.save()
        return HttpResponse('Thank you for your email confimation')
    else:
        return HttpResponse('Activation is invalid')
