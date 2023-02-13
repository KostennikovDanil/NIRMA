from django.urls import path
from .views import *

urlpatterns = [
    path('main/<int:status>', get_main, name='main'),
]