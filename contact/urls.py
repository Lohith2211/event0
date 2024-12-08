from django.urls import path
from . import views

urlpatterns = [
    path('contact-event/', views.events_contact, name='events_contact'),
]
