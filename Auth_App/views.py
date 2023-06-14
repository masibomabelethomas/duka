from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# from django.http import HttpResponse, HttpRequest


# Create your views here.
# {%comments%}
def login_user(request):
    if request.method == 'POST':
    #    from django.contrib.auth import authenticate, login
        username = request.POST.get("Username", None)
        password = request.POST.get("password", None)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # messages.success('request', 'Karibu sana!')
            return redirect(reverse('home'))
            # Redirect to a success page.
        else:
            messages.success('request', 'There was an error login in. Try again..')
            return redirect(reverse('login'))
    else:
        return render(request, 'authenticate/login.html', {})
    # {%comments%}
 