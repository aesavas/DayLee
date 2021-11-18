from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from .utils import create_encrypted_password, check_master_password
from .forms import CustomUserCreationForm
from .models import User, Profile


def create_master_password_view(request):
    page = "create"
    # TODO: Create decorator for this. If do not have master password cannot create diary
    profile = request.user.profile
    if request.method == "POST":
        master_password = create_encrypted_password(request.POST["password"])
        profile.master_password = master_password
        profile.new_user = False
        profile.save()
        messages.success(request, 'Your master password added successfully!')
        return redirect('dashboard')
    context = {
        'page' : page,
    }
    return render(request, 'users/create_or_check_master_password.html', context)

# def check_master_password_view(request, pk):
#     page = 'check'
#     profile = request.user.profile
#     if request.method == "POST":
#         checked = check_master_password(request.POST['password'], profile.master_password)
#         if checked:
#             return redirect(request.path, pk)
#         else:
#             messages.error(request, 'You entered wrong password !')
#     context = {
#         'page':page,
#     }
#     return render(request, 'users/create_or_check_master_password.html', context)

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
            return redirect('login')
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
            if user.profile.new_user:
                return redirect('create-master-password')
            return redirect('dashboard')
        else:
            messages.error(request, 'Username or password is incorrect !')
    return render(request, 'users/login_register.html', context)

def logout_view(request):
    logout(request)
    messages.success(request, 'User was logged out succesfully')
    return redirect('landing-page')