from django.urls import path, include
from .views import new_deploy, signup

urlpatterns = [
    path('', new_deploy)
    # Commenting this out to disable client deploy
    #path('signup/', signup, name='signup')
]
