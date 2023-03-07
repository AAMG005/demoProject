from django.urls import path

from . import views 

urlpatterns = [
	path('dhoni/home',views.index, name='index'),
    path('',views.home,name='home'),
    path('addition1', views.addition, name='addition')
]

