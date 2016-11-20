from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms

from core.forms import BootstrapFormMixin

class LoginForm(BootstrapFormMixin, AuthenticationForm):
	pass

class UserRegistrationForm(BootstrapFormMixin, forms.ModelForm):
    email = forms.CharField(label="Email Address",widget=forms.TextInput(attrs={'placeholder': 'SirSpam@Alot.com'}))
    username = forms.CharField(label="Username",widget=forms.TextInput(attrs={'placeholder': 'SirSpamAlot'}))
    first_name = forms.CharField(label="First_name",widget=forms.TextInput(attrs={'placeholder': 'Jay'}))
    last_name = forms.CharField(label="Last Name",widget=forms.TextInput(attrs={'placeholder': 'Willey'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'placeholder': '*****************'}))
    password2 = forms.CharField(label="Repeat Password", widget=forms.PasswordInput(attrs={'placeholder': '*****************'}))

    class Meta:
	    model = User
	    fields = ('email', 'username', 'first_name', 'last_name', 'password', 'password2',)

    def clean_password2(self):
        cd = self.cleaned_data

        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords Do Not Match')

            return cd['password2']
