from django.urls import path
from .views import *

urlpatterns = [
    path('',home, name='home'),
    path('CheckURL/',url_check, name='url_check'),
    path('prediction/',predict, name='predict'),
]