from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()


#Meta class gives us the nested namespace for
#configurations(which model is affected and so on)and keeps
#the configurations at one place
    class Meta:
        model = User
        #when we say form.save, it's saved with user model
        fields = ['username','email','password1','password2']
