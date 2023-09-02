
from django.contrib import admin
from .models import users_manager

# Register your models here.
admin.site.register(users_manager)
admin.site.register(User)

# admin.site.register(CustomUser)