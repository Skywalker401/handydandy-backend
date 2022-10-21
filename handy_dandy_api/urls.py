from django.urls import path
from .views import UserList, UserDetail
from . import views

urlpatterns = [
    path('', UserList.as_view(), name='user_list'),
    path('<int:pk>', UserDetail.as_view(), name='user_detail'),
    path('api/public', views.public),
    path('api/private', views.private),
    path('api/private-scoped', views.private_scoped),
]
