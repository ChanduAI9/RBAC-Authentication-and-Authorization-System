from django.http import JsonResponse
from functools import wraps
from users.models import User

# Decorator to check if the user has the required permission
def has_permission(permission_name):
    def decorator(func):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            # Get the user from the request object
            user = request.user

            if user.is_authenticated and user.has_permission(permission_name):
                return func(request, *args, **kwargs)  # Allow access if permission exists
            else:
                return JsonResponse({'error': 'Forbidden'}, status=403)  # Deny access
        return wrapper
    return decorator
