from django.conf.urls import url

from . import views
from django.urls import path

urlpatterns = [
    path('', views.UsersListView.as_view(), name='users_list'),
    path('generate/', views.GenerateRandomUserView.as_view(), name='generate'),
]