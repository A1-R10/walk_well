from django.urls import path
from . import views

urlpatterns = [
	path('create/', views.add_post, name='add_post'),
]