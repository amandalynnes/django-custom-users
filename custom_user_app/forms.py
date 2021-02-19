from django import forms
from .models import MyCustomUser

# class AddCustomUser(forms.Form):
#     Display_name = forms.CharField(max_length=40)
#     Age = forms.IntegerField()
#     REQUIRED_FIELDS = ['Display_name', 'Age']
class AddCustomUser(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = MyCustomUser
        fields = (
            'username',
            'Display_name',
        )

class LoginForm(forms.Form):
    username = forms.CharField(max_length=40)
    password = forms.CharField(widget=forms.PasswordInput)