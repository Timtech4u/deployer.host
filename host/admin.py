from django.contrib import admin
from .models import User, Profile, Deploy

admin.site.register(Profile)
admin.site.register(Deploy)