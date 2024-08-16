from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        message = "You are logged in! This is the server"
    else:
        # Redirect to the login page if not authenticated
        # Assuming 'login' is the name of your login URL pattern
        return redirect('login')
        
    return HttpResponse(message)

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', '/')
            return redirect(next_url)
        else:
            return HttpResponse("Invalid credentials")

    # Render login form
    return render(request, 'login.html')
