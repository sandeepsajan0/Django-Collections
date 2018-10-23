from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from . import views

# Login, Logout are in built in django. we can use it directly with the template.
# Register and Profile classes are used for render the templates related to those.
urlpatterns = [
    path('register/',views.Register.as_view()),
    path('login/',LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',LogoutView.as_view(template_name='logout.html')),
    path('profile/',views.Profile.as_view()),
]

