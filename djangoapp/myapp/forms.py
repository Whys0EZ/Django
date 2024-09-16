from django import forms
import re
from django.contrib.auth.models import User

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Tài khoản', max_length=150)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Mật khẩu', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Nhập lại mật khẩu', widget=forms.PasswordInput())

    def clean_password2(self):
        
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 == password2 and password1 and password2:
            return password2
        raise forms.ValidationError("Mật khẩu không hợp lệ")

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not re.search(r'^[\w]+$', username):
            raise forms.ValidationError("Tên tài khoản chỉ được chứa chữ cái, chữ số và gạch dưới.")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Tài khoản đã tồn tại.")
        return username
    
    def save(self):
        User.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data['email'], password=self.cleaned_data['password1'])
        # User.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data['email'], password=self.cleaned_data['password1'])


class LoginForm(forms.Form):
    username = forms.CharField(label='Tài khoản', max_length=150)
    password = forms.CharField(label='Mật khẩu', widget=forms.PasswordInput())

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^[\w]+$', username):
            raise forms.ValidationError("Tên tài khoản có kí tự đặc biệt")
        # if User.objects.filter(username=username).exists():
        return username
        # raise forms.ValidationError("Tài khoản chưa tồn tại.")
        


class SearchForm(forms.Form):
    search = forms.CharField(max_length=150)
    def search_info(self):
        search = self.cleaned_data['search']
        return search