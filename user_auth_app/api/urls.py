from django.urls import path
from .views import UsersView, UsersDetail, LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('users/', UsersView.as_view(), name='users'),
    path('users/<int:pk>/', UsersDetail.as_view(), name='users-detail'),
]