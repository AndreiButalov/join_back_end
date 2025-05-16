from django.urls import path
from .views import UsersView, GuestContactsView, TasksView, TasksDetail, GuestContactsDetail

urlpatterns = [
    path('users/', UsersView.as_view()),          
    path('guestContacts/', GuestContactsView.as_view()),          
    path('guestContacts/<int:pk>/', GuestContactsDetail.as_view(), name='guestContacts-detail'),             
    path('tasks/', TasksView.as_view()),          
    path('tasks/<int:pk>/', TasksDetail.as_view(), name='tasks-detail'),          
]
