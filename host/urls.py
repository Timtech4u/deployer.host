from django.urls import path, include
from .views import new_deploy

urlpatterns = [
    path('', new_deploy),
]