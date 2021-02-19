from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from custom_user_app.models import MyCustomUser

# Register your models here.

class MyCustomUserAdmin(UserAdmin):
    fieldsets = [
        (None, {'fields': ['username']}),
        (None, {'fields': ['password']}),
        (None, {'fields': ['Display_name']}),
        (None, {'fields': ['Age']}),
        (None, {'fields': ['Homepage']}),

    ]

admin.site.register(MyCustomUser, MyCustomUserAdmin)
