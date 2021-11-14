from django.shortcuts import redirect, render


from .forms import CustomUserCreationForm
from .models import Profile



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
