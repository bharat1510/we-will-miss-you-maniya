
from django.shortcuts import render, redirect

class authenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    
    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_authenticated:
            pass
        else:
            return render(request, 'authentication/login.html')
        
        return response

