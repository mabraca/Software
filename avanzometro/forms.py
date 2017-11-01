from django import forms 
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class RegistrationForm(forms.Form):
	username = forms.CharField(label='Username', max_length=30)
	nombre = forms.CharField(label='Nombre', max_length=30)
	apellido = forms.CharField(label='Apellido', max_length=30)
	email = forms.EmailField(label='Email')
	password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput())
	password2 = forms.CharField(label='Confirmar contraseña',widget=forms.PasswordInput())


	def clean_password2(self):
		if 'password1' in self.cleaned_data:
			password1 = self.cleaned_data['password1']
			password2 = self.cleaned_data['password2']
			if password1 == password2:
				return password2
			raise forms.ValidationError('Las contraseñas no coinciden')

	def clean_username(self):
		username = self.cleaned_data['username']
		if not re.search(r'^\w+$', username):
			raise forms.ValidationError('Username solo puede contener caracteres y guion bajo "_" ')
		try:
			User.objects.get(username=username)
		except ObjectDoesNotExist:
			return username
		raise forms.ValidationError('Ese Username no esta disponible.')