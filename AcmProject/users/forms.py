from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(
        attrs={'class': 'input input-bordered input-secondary w-full max-w-xs rounded-lg'}))
    username = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'input input-bordered input-secondary w-full max-w-xs rounded-lg'}))
    password1 = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'input input-bordered input-secondary w-full max-w-xs rounded-lg'}))
    password2 = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'input input-bordered input-secondary w-full max-w-xsrounded-lg'}))

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')

     
    def save(self,commit=True):
        print("saving")
        user=super(NewUserForm,self).save(commit=False)
        user.email=self.cleaned_data['email']
        if commit:
            user.save()
        return user       