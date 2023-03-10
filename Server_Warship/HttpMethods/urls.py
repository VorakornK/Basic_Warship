from HttpMethods import views
from django.urls import path

urlpatterns = [
    path('view/', views.index),
    path('first/', views.first),
    path('start_game/', views.start_game),
    path('create_board/', views.create_board),
    path('join_board/', views.join_board),
    path('send_status/', views.send_status),
    path('send_choice/', views.send_choice),
]
