from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def registerUser(request):
    form = UserCreationForm()

    if request.method == 'POST':
        pass

    if request.method == 'GET':
        context = {'form': form}

    

    return render(request, 'accounts/register.html', context)