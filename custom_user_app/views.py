from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from custom_user_app.models import MyCustomUser
from custom_user_app.forms import AddCustomUser, LoginForm
from django.contrib.auth import settings

# Create your views here.

@login_required()
def index_view(request):
    custom_user_info = MyCustomUser(request)
    auth_user_model = settings.AUTH_USER_MODEL

    return render(request, "index.html", {
        "heading": "Logged-in Users!",
        "custom_user": custom_user_info,
        "auth_user_model": auth_user_model,
    })


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password']
            )
            if user:
                login(request, user)
            return HttpResponseRedirect(reverse('home'))


    form = LoginForm()
    return render(request, "genericform_view.html", {'form': form})


def signup_view(request):
        if request.method == 'POST':
            form = AddCustomUser(request.POST)

            if form.is_valid():
                data = form.cleaned_data
                new_user = MyCustomUser.objects.create(
                    Display_name=data['Display_name'],
                    # Age=data['Age'],
                    username=data['username'],
                    password=data['password'],
                    )
                return HttpResponseRedirect(reverse('home', args=['login/']))

        form = AddCustomUser()
        return render(request, 'genericform_view.html', {'form': form})



