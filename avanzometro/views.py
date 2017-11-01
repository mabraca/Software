from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.template import RequestContext
from django.shortcuts import render_to_response
from avanzometro.forms import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

from avanzometro.forms import UserForm

def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print (True)
            #print user_form.errors
    else:
        user_form = UserForm()
    return render_to_response(
            'template/login.html',
            {'user_form': user_form,  'registered': registered},
            context)

@login_required
def home(request):
    return render_to_response(
    'main_page.html',
    { 'user': request.user }
    )
def main_page(request):
    template = render_to_string('main_page.html', { 'user': request.user })
    return HttpResponse(template)

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
    
def login(request):
    return render_to_response(context_instance=RequestContext(request))

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