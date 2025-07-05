from django.urls import path
from .views import *

urlpatterns = [
    path('register/', registration, name='register'),
    path('auth/', authentication, name='auth'),
    path('logs/', logs, name='logs'),
]
