from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Question
from django.forms import ModelForm


class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email'] 


class LoginForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2']


class QuestionAddingForm(ModelForm):
    class Meta:
        model=Question
        fields="__all__"