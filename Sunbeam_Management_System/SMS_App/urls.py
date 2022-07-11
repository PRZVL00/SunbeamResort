from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('homepage', views.homepage, name='homepage'),
    path('c_reservation', views.c_reservation, name='Reservation'),
    path('billing', views.billing, name='billing'),
    path('confirmation', views.confirmation, name='confirmation'),
    path('login', views.login1, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('signup', views.signup, name='signup'),
    path('reservation', views.reservation, name='reservation'),
    path('booking', views.booking, name='booking'),
    path('walk_ins', views.walk_ins, name='walk_ins'),
    path('inventory', views.inventory, name='inventory'),
    path('rooms', views.room, name='rooms'),
    path('sales', views.sales, name='sales'),
    path('feedback', views.feedback, name='feedback'),
]
