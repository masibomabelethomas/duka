from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# from django.http import HttpResponse, HttpRequest

def login_user(request):
    if request.method == 'POST':
    #    from django.contrib.auth import authenticate, login
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # messages.success('request', 'Karibu sana!')
            return redirect('products')
            # Redirect to a success page.
        else:
            messages.success(request, 'There was an error login in. Try again..')
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})
    


def logout_user(request):
    logout(request)
    messages.success(request, ('you were looged out')) 
    return redirect('home')
 