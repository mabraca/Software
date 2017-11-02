from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from avanzometro.forms import UserRegistrationForm
from django.template.loader import render_to_string
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'main_page.html')
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                login(request, user)
                return HttpResponseRedirect('registration/login.html')
            else:
                raise forms.ValidationError('El usuario ya existe!')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/login.html', {'form' : form})

def main_page(request):
    template = render_to_string('main_page.html', { 'user': request.user })
    return HttpResponse(template)

def index_page(request):
    template = render_to_string('form.html', { 'user': request.user })
    return HttpResponse(template)

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('main_page.html')
    

