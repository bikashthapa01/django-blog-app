from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm 
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views import generic 


# Create your views here

def index(request):
	return HttpResponse('Heya, Explorer ? ')

class RegisterUserView(generic.CreateView):
	form_class = UserCreationForm	
	template_name = 'register.html'
	success_url = reverse_lazy('login')
