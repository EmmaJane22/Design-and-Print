from django.urls import path
from . import views

urlpatterns = [
    path('', views.bespoke_orders, name='bespoke'),
    
]
