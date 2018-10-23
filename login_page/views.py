from django.shortcuts import render
from django.views.generic import TemplateView
from .models import RegistrationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class Register(TemplateView):
    """
    Register class is used for Registration proceess.
    In post method, it will take all data entered in form and save it in database(form.save())
    And In get method, It will only return the form to fill the detail or to register.
    """
    template_name = 'registration.html'
    
    def post(self,request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            form = RegistrationForm()
        return render(request,self.template_name,{'form':form})
    def get(self,request):
        form=RegistrationForm()
        return render(request,self.template_name,{'form':form})


class Profile(TemplateView):
    """
    Profile class is used for render the template "profile.html".
    @method_decorator is used to authenticate user or user can see proflie only after the logged in.
    """
    template_name = 'profile.html'
    @method_decorator(login_required)
    def get(self,request):
        return render(request,self.template_name)
