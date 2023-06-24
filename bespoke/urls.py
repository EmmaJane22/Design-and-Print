from django.urls import path
from . import views

urlpatterns = [
    path('', views.bespoke_orders, name='bespoke'),
    path('<int:bespoke_order_id>/', views.bespoke_order_detail, name='bespoke_order_detail'),
    path('add/', views.add_bespoke_order, name='add_bespoke_order'),
    path('quote/<int:bespoke_order_id>/', views.quote_bespoke_order, name='quote_bespoke_order'),
    path('accept/<int:bespoke_order_id>/', views.accept_bespoke_order, name='accept_bespoke_order'),
    path('delete/<int:bespoke_order_id>/', views.delete_bespoke_order, name='delete_bespoke_order'),
]
