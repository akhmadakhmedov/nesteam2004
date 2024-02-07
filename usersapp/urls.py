from django.urls import path
from .views import *

urlpatterns = [
    path('list/', users_list, name='users-list'),
    path('detail/<int:pk>/', user_detail, name="user-detail"),

]