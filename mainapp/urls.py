from django.urls import path
from .views import (
	home)
from . import views as mainapp_views
urlpatterns = [
	 path('',mainapp_views.home, name='mainapp-home'),
	 path('blog/',mainapp_views.blog, name='mainapp-blog'),
	 path('blogpage/',mainapp_views.blogpage, name='mainapp-blogpage'),
	 path('contact/',mainapp_views.contact, name='mainapp-contact'),
	 path('services/',mainapp_views.services, name='mainapp-services'),
	 path('doctors/',mainapp_views.doctors, name='mainapp-doctors'),
	 path('about/',mainapp_views.about, name='mainapp-about'),

	]

