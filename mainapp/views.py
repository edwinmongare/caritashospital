from django.shortcuts import render
from django.http import HttpResponseRedirect

# Creatoge your views here.

def home(request):
	return render(request, 'mainapp/index.html')

def blog(request):
	return render(request, 'mainapp/blog.html')

def blogpage(request):
	return render(request, 'mainapp/blog-single.html')

def contact(request):
	return render(request, 'mainapp/contact.html')

def services(request):
	return render(request, 'mainapp/services.html')

def doctors(request):
	return render(request, 'mainapp/doctors.html')

def about(request):
	return render(request, 'mainapp/about.html')