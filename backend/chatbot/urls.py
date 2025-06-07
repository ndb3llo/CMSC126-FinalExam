from django.urls import path
from .views import chatbot_api

urlpatterns = [
    path('chatbot_api/', chatbot_api),
]