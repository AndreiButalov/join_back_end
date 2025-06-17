from django.urls import path
from .views import GuestContactsView, TasksView, TasksDetail, GuestContactsDetail, SubTasksView, SubTasksDetail

urlpatterns = [
    path('guestContacts/', GuestContactsView.as_view()),          
    path('guestContacts/<int:pk>/', GuestContactsDetail.as_view(), name='guestContacts-detail'),             
    path('tasks/', TasksView.as_view()),          
    path('tasks/<int:pk>/', TasksDetail.as_view(), name='subtasks-detail'),          
    path('subtasks/', SubTasksView.as_view()),          
    path('subtasks/<int:pk>/', SubTasksDetail.as_view(), name='subtasks-detail'),          
]
