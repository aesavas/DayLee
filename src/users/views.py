from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from .forms import CustomUserCreationForm
from .models import User, Profile



def register_profile_view(request):
    form = CustomUserCreationForm()
    page = 'register' #! It show type of page.
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'User account was created successfully!')
            return redirect('dashboard')
        else:
            messages.error(request, 'An error has occurred during registration!')
    context = {
        'form' : form,
        'page' : page,
    }
    return render(request, 'users/login_register.html', context)


def login_view(request):
    page = 'login'
    context = {
        'page' : page,
    }

    # TODO: check with is_authenticated, if True then redirect somewhere if not then redirect login page

    if request.method == "POST":
        username = request.POST['username'].lower()
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist!')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'User has been login successfully!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Username or password is incorrect !')
    return render(request, 'users/login_register.html', context)

def logout_view(request):
    logout(request)
    messages.success(request, 'User was logged out succesfully')
    return redirect('landing-page')