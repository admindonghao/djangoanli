from django import forms


# 注册表单类
class RegFrom(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'用户名', 'required':'required',}),
                               max_length=50, error_messages={'required':'用户名不能为空',})
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'邮箱', 'required':'required',}),
                             max_length=50, error_messages={'required':'邮箱不能为空'})
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'密码', 'required':'required',}),
                               max_length=50, error_messages={'required':'密码不能为空'})
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'请确认密码', 'required':'required',}),
                               max_length=50, error_messages={'required':'密码不能为空'})

    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError('所有项为必填项')
        elif self.cleaned_data['password2'] != self.cleaned_data['password']:
            raise forms.ValidationError('两次输入密码不一致')
        else:
            cleaned_data = super(RegFrom,self).clean()
        return cleaned_data


# 登录表单类
class LoginFrom(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholer':'用户名', 'required':'required',}),
                               max_length=50, error_messages={'required':'用户名不能为空'})
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholer':'密码', 'required':'required'}),
                               max_length=50, error_messages={'required':'密码不能为空'})

    def clean(self):
        if not self.is_valid():
            raise  forms.ValidationError('所有项都不能为空')
        else:
            cleaned_data = super(LoginFrom, self).clean()
        return cleaned_data


