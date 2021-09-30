from django.contrib import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login as dj_login, authenticate,logout
from  users.models import *
from users.forms import *
# Create your views here.

def login(request):
	context = {}

	user = request.user
	if user.is_authenticated:
		return redirect("home")

	destination = get_redirect_if_exists(request)
	print("destination: " + str(destination))

	if request.POST:
		form = AccountAuthenticationForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)

			if user:
				dj_login(request, user)
				messages.success(request,'You are logged in successfully')
				if destination:
					return redirect(destination)
				return redirect("home")

	else:
		form = AccountAuthenticationForm()

	context['login_form'] = form

	return render(request, "user/login.html", context)     
    #return render(request, 'users/login.html')

def register_view(request):
	if request.user.is_authenticated: 
		return HttpResponse("You are already authenticated as " + str(request.user.email))

	context = {}
	if request.POST:
		print("post request",request.POST)
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
		else:
			context['registration_form'] = form

	else:
		form = RegistrationForm()
		context['registration_form'] = form
		return render(request, 'user/register.html',context)
	return render(request, 'user/register.html',context)

def get_redirect_if_exists(request):
	redirect = None
	if request.GET:
		if request.GET.get("next"):
			redirect = str(request.GET.get("next"))
	return redirect



# Logout 
def logout_view(request):
	logout(request)
	messages.success(request,'You are log out successfully')
	return redirect('home')

