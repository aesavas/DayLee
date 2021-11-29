from django.contrib import messages
from django.urls import reverse
from functools import wraps
from django.shortcuts import redirect, render
from users.utils import check_master_password
from users.views import check_master_password_view



def master_password_required(view_func):
    @wraps(view_func)
    def decorator(request, *args, **kwargs):
        if request.session['master_password_provided']:
            return view_func(request, *args, **kwargs)
        return redirect('check-master-password')
    return decorator

