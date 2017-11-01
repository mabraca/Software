from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.template import RequestContext
from django.shortcuts import render_to_response
from avanzometro.forms import *

def main_page(request):
    template = render_to_string('main_page.html', { 'user': request.user })
    return HttpResponse(template)

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'], nombre=form.cleaned_data['nombre'], apellido=form.cleaned_data['apellido'],email=form.cleaned_data['email'],password=form.cleaned_data['password1'])
            return HttpResponseRedirect('/main_page.html')
    form = RegistrationForm()
    #variables = RequestContext(request, {'form': form})
    return render(request, 'registration/login.html', {'form': form})
    #render_to_response('registration/register.html',variables)

#def main_page(request):
#    return render_to_response('home.html', RequestContext(request))