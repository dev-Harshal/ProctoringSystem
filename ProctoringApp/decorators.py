from functools import wraps
from django.shortcuts import redirect

def login_required_teacher():
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('login')  # Redirect to login page if user is not authenticated
            else:
                if request.user.role == "Student":
                    return redirect('student-dashboard')

            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator