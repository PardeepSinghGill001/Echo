from django import forms 
from .models import Buzz
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BuzzForm(forms.ModelForm):
    class Meta:
        model = Buzz
        fields = ['text','photo']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username','email','password1','password2')