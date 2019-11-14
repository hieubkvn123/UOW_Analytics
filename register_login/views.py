from django.shortcuts import render, redirect
from . import forms
from .models import Account, Info
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse

# Create your views here.
def home(response):
    if response.session['username'] == None:
        return redirect(register)
    else:
        return redirect(load_account)

def register(response):
    if response.method == 'POST': # if form submitted
        form = forms.Register(response.POST)
        if(form.is_valid()):
            username = form.cleaned_data['username']
            account = ''
            try:
                account = Account.objects.get(username=username)

                form = forms.Register()
                return render(response, 'register_login/register.html', {'form':form,'msg_type':'error','msg':'The provided username has been taken'})
            except ObjectDoesNotExist:
                try:
                    first_name = form.cleaned_data['first_name']
                    last_name = form.cleaned_data['last_name']
                    major = form.cleaned_data['major']
                    faculty = form.cleaned_data['faculty']

                    username = form.cleaned_data['username']
                    password = form.cleaned_data['password']

                    account = Account.objects.create(username=username, password=password)
                    account.info_set.create(first_name=first_name, last_name=last_name, major=major, faculty=faculty)

                    form = forms.Register()
                    # form with message
                    return render(response, 'register_login/register.html', {'form':form,'msg_type':'success','msg':'Regsitration successful'})
                except Exception:
                    form = forms.Register()
                    # form with message
                    return render(response, 'register_login/register.html', {'form':form,'msg_type':'error','msg':'Something went wrong with your registration'})

    else: # if form not submitted
        form = forms.Register()
        return render(response, 'register_login/register.html', {'form':form}) # brand new form without message

def login(response):
    if(response.method == 'POST'):
        form = forms.Login(response.POST)

        if(form.is_valid()):
            username = form.cleaned_data['username']
            account = ''
            try: # if the account exists
                account = Account.objects.get(username=username)
                password = account.password

                input_pwd = form.cleaned_data['password']
                if(input_pwd == password):
                    response.session['username'] = account.username
                    info = account.info_set.all()[0]
                    first_name = info.first_name
                    last_name = info.last_name
                    full_name = first_name + ' ' + last_name
                    response.session['fullname'] = full_name

                    return redirect(load_account)
                else:
                    return render(response, 'register_login/login.html', {'form':form, 'msg_type':'error', 'msg':'Password incorrect'})

            except ObjectDoesNotExist:
                form = forms.Login()
                return render(response, 'register_login/login.html', {'form':form, 'msg_type':'error', 'msg':'Username does not exists'})
    else:
        form = forms.Login()
        return render(response, 'register_login/login.html', {'form':form})

def load_account(response):
    try:
        username = response.session['username']
        fullname = response.session['fullname']

        return render(response, 'register_login/account.html', {'fullname':fullname,'welcome':True})
    except Exception:
        return redirect(register)

def logout(response):
    # Reseting the two sessions
    response.session['username'] = None
    response.session['fullname'] = None

    return redirect(register) # redirecting to registration page
