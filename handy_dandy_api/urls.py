from django.urls import path
from .views import UserList, UserDetail, public, private, private_scoped

urlpatterns = [
    path('', UserList.as_view(), name='user_list'),
    path('<int:pk>', UserDetail.as_view(), name='user_detail'),
    path('public', public),
    path('private', private),
    path('private-scoped', private_scoped),
]
