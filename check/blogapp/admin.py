from django.contrib import admin
from .models import *
from django.contrib.sessions.models import Session


admin.site.register(Blog)
admin.site.register(Profile)
admin.site.register(Session)
