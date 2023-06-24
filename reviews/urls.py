from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_reviews, name='reviews'),
    path('delete/<int:review_id>/', views.delete_review, name='delete_review'),
    path('add/', views.add_review, name='add_review'),
]
