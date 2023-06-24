from django.urls import path
from . import views

urlpatterns = [
    path('', views.bespoke_orders, name='bespoke'),
    path('<int:bespoke_order_id>/', views.bespoke_order_detail, name='bespoke_order_detail'),
    path('add/', views.add_bespoke_order, name='add_bespoke_order'),
    
]
