from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect
# Create your views here.
def registerUser(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('User created successfully')


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
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context=context)



def home(request):
    return render(request, 'accounts/home.html')

def logoutUser(request):
    logout(request)
    return redirect('home')