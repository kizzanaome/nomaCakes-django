from ..models import User
from django.db import IntegrityError
from rest_framework import serializers
import re


def validate_username(username):

    check_user  = User.objects.filter(username=username)
    if check_user.exists():
        raise serializers.ValidationError(f"A user with username {username} already exists")
    username = username
    if len(username.strip()) < 5:
        raise serializers.ValidationError("The username should be longer than 5 characters")
    return username

def validate_password(password):

    if len(password) < 7:
        raise serializers.ValidationError("The password should be 7 characters long")
    if re.search(r'(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])', password) is None:
        raise serializers.ValidationError("The password should have a capital letter, small letter and a number")
    return password

def validate_email(email):

    check_email = User.objects.filter(email=email)
    if check_email.exists():
        raise serializers.ValidationError(f"A user with email {email} already exists.")
    return email

def validate_contact(contact):

    check_contact = User.objects.filter(contact=contact)
    if check_contact.exists():
        raise serializers.ValidationError("A user with that contact already exists")
    if not re.search(r"^[+]\d{3}[-]\d{9}$", contact):
            raise serializers.ValidationError("Contact should be in this format '+xxx-xxxxxxxxx'")
    return contact
