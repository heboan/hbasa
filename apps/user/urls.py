from django.urls import path
from .views import UserGroupView

app_name = 'user'

urlpatterns = [
    path('user_group', UserGroupView.as_view(), name='user_group'),
]