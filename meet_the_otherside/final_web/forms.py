from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Post
class RegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email",widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}))
    firstname = forms.CharField(label = "First name",widget=forms.TextInput(attrs={'placeholder': 'Enter your first name'}))
    lastname = forms.CharField(label = "Last name",widget=forms.TextInput(attrs={'placeholder': 'Enter your last name'}))
    username = forms.CharField(label = "User name",widget=forms.TextInput(attrs={'placeholder': 'Enter your user name'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'}))
    class Meta:
        model = User
        fields = ("username", "firstname", "lastname", "email", )

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        firstname = self.cleaned_data["firstname"]
        lastname = self.cleaned_data["lastname"]
        user.first_name = firstname
        user.last_name = lastname
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
    
class PostForm(forms.ModelForm):
    text = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'placeholder': 'What\'s on your mind?', 'onchange': 'character_count()', 'onkeypress': 'character_count()', 'onfocus': 'character_count()' ,'oninput': 'character_count()', 'onkeyup':'character_count()','onpaste':'character_count()'}))
    anonymous = forms.BooleanField(required=False)
    images = forms.ImageField(required=False,widget=forms.ClearableFileInput(attrs={'multiple': True, 'onchange': 'previewImages(this)'}))
    class Meta:
        model = Post
        fields = ("text", "anonymous", )