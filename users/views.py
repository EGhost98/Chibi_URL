from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
        else:
            if 'username' in form.errors:
                messages.warning(request, 'Username already exists. Please choose a different username.')
            if form.errors.get('password2') == ['The two password fields didn’t match.']:
                messages.warning(request, 'Passwords do not match. Please enter the same password in both fields.')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})