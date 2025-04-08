from django.urls import path
from .views import SentimentView, TestView

urlpatterns = [
    path('sentiment/', SentimentView.as_view(), name='sentiment'),
    path('test/', TestView.as_view(), name='test'),
]