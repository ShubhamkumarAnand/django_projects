from django.urls import path
from links.views import index

urlpatterns = [
    path('', index),
]
