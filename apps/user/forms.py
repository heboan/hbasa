from utils.form import FormMixin
from django import forms
from  django.core import validators


class LoginForm(FormMixin):
    username = forms.CharField(max_length=20, min_length=3, error_messages={
        "required": "用户名是必填字段",
        "max_length": "用户名长度为3-20",
        "min_length": "用户名长度为3-20"
    })
    password = forms.CharField(max_length=24, min_length=6, error_messages={
        "required": "密码是必填字段",
        "max_length": "，密码长度为6-24",
        "min_length": "密码长度为6-24"
    })


class ModifyPwdForm(FormMixin):
    oldpwd = forms.CharField(max_length=24, min_length=6, error_messages={
        "required": "旧密码是必填字段",
        "max_length": "旧密码长度为6-24",
        "min_length": "旧密码长度为6-24"
    })
    pwd1 = forms.CharField(max_length=24, min_length=6, error_messages={
        "required": "新密码是必填字段",
        "max_length": "旧密码长度为6-24",
        "min_length": "旧密码长度为6-24"
    })
    pwd2 = forms.CharField(required=True, error_messages={"required": "确认新密码是必填字段"})

    def clean(self):
        cleaned_data = super().clean()
        pwd1 = cleaned_data.get('pwd1')
        pwd2 = cleaned_data.get('pwd2')
        if pwd1 != pwd2:
            raise  forms.ValidationError('新密码输入不一致')