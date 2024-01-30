from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

@csrf_exempt
def clogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome, {user.username}!")
                return redirect('index')
        else:
            # If the form is invalid, display custom error messages
            errors = form.errors.as_data()
            error_messages = []
            for field, field_errors in errors.items():
                for error in field_errors:
                    if field == 'username':
                        error_messages.append("Username does not exist.")
                    elif field == 'password':
                        error_messages.append("Incorrect password.")
                    else:
                        error_messages.append(error.message)
    else:
        form = AuthenticationForm()
        error_messages = None
    return render(request, 'users/login.html', {'form': form, 'error_messages': error_messages, 'show_welcome_notification': True})


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