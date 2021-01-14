"""DjangoREST URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path, include
from .settings import MEDIA_ROOT
from django.views.static import serve
from user.views import IndexView, LoginView, LogoutView, ProfileView, ModifyPwdView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile', ProfileView.as_view(), name='profile'),
    path('modify_pwd', ModifyPwdView.as_view(), name='modifypwd'),
    path('user/', include('user.urls', namespace='user')),
    re_path('media/(?P<path>.*)', serve, {'document_root':MEDIA_ROOT})

]
