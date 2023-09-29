from django.shortcuts import redirect
from django.contrib import messages

def login_required_for_registration(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.error('You must be NOT logged in to sign up')
            return redirect('login')
        else:
            return view_func(request, *args, **kwargs)
    return _wrapped_view
