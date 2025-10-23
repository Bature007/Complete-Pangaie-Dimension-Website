from django import forms
from .models import Form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 
from .models import Post,Form
from django.contrib.auth.forms import AuthenticationForm 
from django.forms.widgets import PasswordInput,TextInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field

#model for contact form
class Contactform(forms.ModelForm):
    class Meta:
        model=Form
        fields=['fullname','email','phone_number','message']


    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.layout = Layout(
                Field('fullname'),
                Field('email'),
                Field('phone_number'),
                Field('message'),
            )

    # widgets = {
    #         'fullname': forms.TextInput(attrs={'placeholder': 'Enter Name'}),
    #         'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
    #         'phone_number': forms.TextInput(attrs={'placeholder': 'Phone'}),
    #         'message': forms.Textarea(attrs={'placeholder': 'Enter Message'}),
    # }






# images=forms.ImageField(widget=forms.ImageInput(attrs={'class':'form-control'}))


# model for postf
class Postform(forms.ModelForm):
    class Meta:
        model=Post
        fields=['author','title','post','image','slug','date']
        # fields='__all__'

    author=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    title=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    post = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    image=forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    # video = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    slug = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control','type': 'date'}))


#model for update
class updateform(forms.ModelForm):
    class Meta:
        model=Post
        # fields=['author','title','post','image','video']
        fields='__all__'

    author=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    title=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    post = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    image=forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    video = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    slug = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control','type': 'date'}))

# model for registration form
class Regform(UserCreationForm):
    email=forms.EmailField(required=True)

    class Meta:
        model=User
        fields=['username','email','password1','password2']
    
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class Loginform(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    