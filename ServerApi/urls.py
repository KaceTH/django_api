
from django.urls import path

from ServerApi import views

urlpatterns = [
    path('users/', views.user_list),
    # path('users/<int:pk>/', views.user),
    path('users/<user_id>/', views.user),
    path('login/', views.login),
]
