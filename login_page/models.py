from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
# Create your models here.


# RegistrationForm is a form which is using in built model "User" and its field.
class RegistrationForm(UserCreationForm):
	email = forms.EmailField(required = True,help_text='Required')
	
	class Meta:
		model = User
		fields = (
			"username",
			"first_name",
			"last_name",
			"email",
			"password1",
			"password2"
		)
	
	def save(self,commit = True):
		user = super(RegistrationForm, self).save(commit = False)
		user.first_name = self.cleaned_data["first_name"]
		user.last_name = self.cleaned_data["last_name"]
		user.email = self.cleaned_data["email"]
		
		if commit:
			user.save()
		return user
