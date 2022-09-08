from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from . import models

# Register your models here.

@admin.register(models.User)
class CustomUserAdmin(UserAdmin ): #admin.site.register(models.User, CustomUserAdmin)과 같음
    
    """Cuestom User Admin"""

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile", #파란색 칸의 제목
            {
                "fields": (
                    "avatar" ,
                    "gender",
                    "bio", 
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            }
        ),
    )

    list_display = ('username', 'email', 'gender', 'language', 'currency', 'superhost')
    list_filter= ("language", "currency", 'superhost')