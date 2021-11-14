from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout

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
            return redirect('dashboard')
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
            # TODO: Add error message alert
            print('Username does not exist!')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # TODO: Add success message alert
            return redirect('dashboard')
        else:
            pass
            # TODO: Add error message alert
    return render(request, 'users/login_register.html', context)

def logout_view(request):
    logout(request)
    # TODO: Add success message alert
    return redirect('landing-page')