from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('logout/', views.log_out, name='logout'),
    path('signup/', views.sign_up, name='signup'),
    path('post/', views.post, name='post'),
]