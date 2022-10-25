from django.urls import path
from .views import UserList, UserDetail, public, private, private_scoped, get_user, create_user, TaskList, TaskDetail, ApplianceList, ApplianceDetail, UserList

urlpatterns = [
    path('', UserList.as_view(), name='user_list'),
    path('<int:pk>', UserDetail.as_view(), name='user_detail'),
    path('public', public),
    path('private', private),
    path('private-scoped', private_scoped),
    path('get-user', get_user),
    path('create-user', create_user),
    path('task-list', TaskList.as_view(), name='task_list'),
    path('task/<int:pk>', TaskDetail.as_view(), name='task_detail'),
    path('appliance-list', ApplianceList.as_view(), name='appliance_list'),
    path('appliance/<int:pk>', ApplianceDetail.as_view(), name='appliance_detail'),
    path('user-list', UserList.as_view(), name='user_list'),
]
