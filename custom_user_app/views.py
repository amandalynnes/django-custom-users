from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from custom_user_app.models import MyCustomUser
from django.contrib.auth import settings
# from custom_user_app.forms import AddCustomUser


# Create your views here.

@login_required()
def index_view(request):
    username = MyCustomUser.objects.get().username
    display_nm = MyCustomUser.objects.get().Display_name
    auth_user_model = settings.AUTH_USER_MODEL

    return render(request, "index.html", {
        "heading": "Logged-in Users!",
        "username": username,
        "display_nm": display_nm,
        "auth_user_model": auth_user_model,
    })

