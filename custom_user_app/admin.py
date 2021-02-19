from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from custom_user_app.models import MyCustomUser

# Register your models here.

class MyCustomUserAdmin(UserAdmin):
    fieldsets = [
        (None, {'fields': ['username']}),
        (None, {'fields': ['password']}),
        (None, {'fields': ['display_name']}),
        (None, {'fields': ['age']}),
    ]

admin.site.register(MyCustomUser, MyCustomUserAdmin)
