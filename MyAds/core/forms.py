from django import forms
from .models import MyUser

class CreateUser(forms.Form):
    username = forms.CharField(label="Username",widget=forms.TextInput(attrs={"class":"input"}))
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={"class":"input"}))
    password2 = forms.CharField(label="Password Confirmation",help_text="Resting Password is Impossible so dont forget password",widget=forms.PasswordInput(attrs={"class":"input"}))

    def clean_username(self):
        user = MyUser.objects.filter(username=self.cleaned_data.get("username"))
        if user.exists():
            raise forms.ValidationError("please use another username")
    def clean_password2(self):
        first = self.cleaned_data.get("password1")
        second =self.cleaned_data.get("password2")
        if(first != second):
            raise forms.ValidationError('passwords dont match')
        return first