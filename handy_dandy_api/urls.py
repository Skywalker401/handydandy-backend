from django.urls import path
from .views import UserList, UserDetail, delete_task, public, private, private_scoped, get_user, create_user, create_task, delete_task, get_pros, update_task, TaskList, TaskDetail, UserList

urlpatterns = [
    path('', UserList.as_view(), name='user_list'),
    path('<int:pk>', UserDetail.as_view(), name='user_detail'),
    path('public', public),
    path('private', private),
    path('private-scoped', private_scoped),
    path('get-user', get_user),
    path('get-pros', get_pros),
    path('create-user', create_user),
    path('create-task', create_task),
    path('update-task', update_task),
    path('delete-task', delete_task),
    path('task-list', TaskList.as_view(), name='task_list'),
    path('task/<int:pk>', TaskDetail.as_view(), name='task_detail'),
    path('user-list', UserList.as_view(), name='user_list'),
]
