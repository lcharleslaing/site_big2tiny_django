from django.shortcuts import render, redirect
from account.models import Account
from django.contrib.auth import login, authenticate, logout
from account.forms import RegistrationForm


def account_home_screen_view(request):
    context = {}
    accounts = Account.objects.all()
    context['accounts'] = accounts

    return render(request, "account/home_account.html", context)


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            context['registration_form'] = form
    else:  # GET request
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'account/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')
