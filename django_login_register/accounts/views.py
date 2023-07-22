from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect
from .forms import UpdateUsername, UpdatePassword


# Create your views here.
def registerUser(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')


    context = {'form': form}

    return render(request, 'accounts/register.html', context)

def loginUser(request):

    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)

        username = form.data['username']
        password = form.data['password']

        user = authenticate(request=request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully: welcome :)')
            return redirect('accounts-home')
        else:
            messages.error(request, 'Invalid username or password')
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context=context)



@login_required(login_url='login')
def home(request):
    return render(request, 'accounts/home.html')

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def updateUsername(request):

    form = UpdateUsername()

    if request.method == 'POST':
        form = UpdateUsername(request.POST)

        form_username = form.data['new_username']
        form_confirm_username = form.data['confirm_new_username']
        password = form.data['password']

        user = request.user

        if form_username != form_confirm_username:
            messages.error(request, 'Usernames do not match')
            return redirect('update-username')

        if not(user.check_password(password)):
            messages.error(request, 'Invalid password')
            return redirect('update-username')
        user.username = form_username    
        user.save()
        return redirect('accounts-home')

    context = {
        'form': form
    }
    return render(request, 'accounts/update_username.html', context=context)

@login_required(login_url='login')
def updatePassword(request):

    form = UpdatePassword()

    if request.method == 'POST':
        form = UpdatePassword(request.POST)

        current_password = form.data['current_password']
        new_password = form.data['new_password']
        confirm_new_password = form.data['confirm_new_password']

        user = request.user

        if not(user.check_password(current_password)):
            messages.error(request, 'Invalid password')
            return redirect('update-password')
        
        if new_password != confirm_new_password:
            messages.error(request, 'Passwords do not match')
            return redirect('update-password')
        
        user.set_password(new_password)
        user.save()
        login(request, user)
        return redirect('accounts-home')


    context = {
        'form': form
    }

    return render(request, 'accounts/update_password.html', context=context)