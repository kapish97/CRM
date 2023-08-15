from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserChangeForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email address'}))
    first_name = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First name'}))
    last_name =  forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'last name'}))

    class Meta:
        model = User
        fields = ('username','first_name','email','password1','password2')
