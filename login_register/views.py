from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RegisterForm, LoginForm
from django.contrib.auth.hashers import make_password
from .models import Users
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    return render(request, 'login_register/index.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            fullname = form.cleaned_data['fullname']
            password = form.cleaned_data['password']
            username = form.cleaned_data['username']
            
            
            
            try:
                user = Users.objects.create_user(email=email, full_name=fullname, password=password, username=username)
                user.save()
                messages.success(request,'Registration successful')
                return redirect('login')
            except IntegrityError as e:
                error_message = str(e)
                if 'email_address' in error_message:
                    messages.success(request,'Email address already exists')
                if 'username' in error_message:
                    messages.success(request,'Username already exists')
            
            return redirect('register') 
            
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
                    print(error)
        
                      
    form = RegisterForm()
    response = render(request, 'login_register/register.html', {'form': form})
    return response


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # print(user.id)
                request.session['user_id']=user.pk
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password')
        return redirect('login') 
    else:
        form = LoginForm()
        
    context = {'form': form}
    return render(request, 'login_register/login.html', context)



def profile_view(request):
    return render(request, 'login_register/profile.html')

def logout_view(request):
    logout(request)
    return render(request, 'login_register/login.html')

