from django.urls import path # type: ignore
from .views import appointment

urlpatterns = [
    path('appointment/', appointment, name='appointment'),
]
