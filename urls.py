from django.urls import path     
from . import views


urlpatterns = [
    path('', views.index, name='principal'),
    path('login', views.login, name='login'),    
    path('settings', views.settings, name='settings'),
    path('process_money', views.process_money, name='money'),
    path('reset', views.reset, name='reset')
]

