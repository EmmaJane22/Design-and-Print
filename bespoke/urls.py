from django.urls import path
from . import views

urlpatterns = [
    path('', views.bespoke_products, name='bespoke'),
    path('bespoke/', views.bespoke_products, name='bespoke'),
]
