from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from . import models

# Register your models here.

@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    
    """Cuestom User Admin"""

    list_display = ('username', 'email', 'gender', 'language', 'currency', 'superhost')
    list_filter= ("language", "currency", 'superhost')