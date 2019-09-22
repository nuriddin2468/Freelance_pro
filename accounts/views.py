from django.shortcuts import render
from django.views import generic
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth import logout
# Create your views here.


class LoginView(generic.View):

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        next_url = request.POST['next']
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
            if not user:
                pass
        return redirect(next_url)


class RegisterView(generic.View):
    pass


def LogoutView(request):
    logout(request)
    return redirect('dashboard')
