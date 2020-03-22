from django.shortcuts import render, redirect
from django.contrib import messages # to include message.debug, message.info, message.success, message.warning, message.error
from .forms import UserRegisterForm
#from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!') # one time flash message [ f''(f-string) supported in python 3.6.x+ only]
            return redirect('blog-home') # after user registration redirect to home page 
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

