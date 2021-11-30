from functools import wraps
from django.shortcuts import redirect



def master_password_required(view_func):
    @wraps(view_func)
    def decorator(request, *args, **kwargs):
        if request.session['master_password_provided']:
            return view_func(request, *args, **kwargs)
        return redirect('check-master-password')
    return decorator

