from django.urls import path, include
from .views import signup_view, login_view

app_name = "authentication"

urlpatterns = [
    path('signup', signup_view, name="signup"),
    path('login', login_view, name='login' )
]
