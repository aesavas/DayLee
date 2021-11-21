from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, SetPasswordForm
from django import forms
from .models import Profile




class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Name',
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'username', 'profile_image']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name,field in self.fields.items():
            if name != 'profile_image':
                field.widget.attrs.update({'class':'form-control'})


class UserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={
            'class':'form-control',
            'placeholder':'Enter your email please..',
            'type':'email',
            'name':'email'
        }))

class UserPasswordSetForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordSetForm, self).__init__(*args, **kwargs)

    new_password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Enter your new password',
    }))

    new_password2 = forms.CharField(label="Password Confirmation", widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Retype your new password',
    }))