from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.contrib.auth.hashers import make_password
from utils import restful
from .models import UserProfile
from .forms import LoginForm, ModifyPwdForm
from utils.login import LoginRequireMixin

# Create your views here.


class IndexView(LoginRequireMixin, View):
    """ Dashboard """

    def get(self, request):
        return render(request, 'index.html')


class ProfileView(LoginRequireMixin, View):
    """ 个人中心 """

    def get(self, request):
        return render(request, 'profile.html')


class CustomBackend(ModelBackend):
    """ 允许用户名或密码登录 """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception:
            return None


class LoginView(View):
    """ 登录 """

    def get(self, request, msg=''):
        return render(request, 'login.html', {
            'msg': msg
        })

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
                else:
                    return self.get(request, msg='该用户已被禁用，请联系管理员')
            return self.get(request, msg='账号或密码错误')
        else:
            msg = form.get_errors()
            return self.get(request, msg)


class LogoutView(LoginRequireMixin, View):
    """ 退出登录 """
    def get(self, request):
        logout(request)
        return redirect('login')


class ModifyPwdView(LoginRequireMixin, View):
    """ 用户修改密码 """
    def post(self, request):
        form = ModifyPwdForm(request.POST)
        if form.is_valid():
            user = request.user
            oldpwd = form.cleaned_data.get('oldpwd')
            newpwd = form.cleaned_data.get('pwd1')

            if not user.check_password(oldpwd):
                return restful.params_error('旧密码错误')
            print(newpwd)
            user.password = make_password(newpwd)
            user.save()
            return restful.success()
        else:
            print(form.get_errors())
            return restful.params_error(message=form.get_errors())


class UserGroupView(LoginRequireMixin, View):
    """用户组"""
    def get(self, request):
        return render(request, 'userGroup.html')