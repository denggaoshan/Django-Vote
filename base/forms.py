#coding:utf_8
from django import forms            
from django.contrib.auth.models import User   # fill in custom user info then save it 
from django.contrib.auth.forms import UserCreationForm  

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True)
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'username'}))
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        error_messages = {
        'duplicate_username': 'my custom error message'
        }

    def save(self,commit = True):   
        user = super(RegistrationForm, self).save(commit = False)
        user.email = self.cleaned_data['email']
        
        
        if commit:
            user.save()

        return user