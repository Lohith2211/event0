from django.urls import path
from .views import create_stream, stream_list

urlpatterns = [
    path('create/', create_stream, name='create_stream'),
    path('', stream_list, name='stream_list'),
]
# livestream/urls.py

