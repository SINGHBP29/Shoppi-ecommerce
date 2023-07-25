from django import forms

# from Dell.models import Login, registrationForm
#from Dell.models import loginForm
#from Dell.models import registrationForm
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm,UsernameField,PasswordChangeForm,SetPasswordForm,PasswordResetForm
from django.contrib.auth.models import User
from . models import Customer
# from django.contrib.auth.forms im



class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus' : 'True', 'class':'form-control','placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control','placeholder':'Password'}))
    
'''class LoginForm(forms.ModelForm):
    Username = forms.EmailField(max_length=63,required=True)
    Password1 = forms.CharField(max_length=83 , widget=forms.PasswordInput,required=True)
    
    class Meta:
        model = Login
        fields = ['Username', 'Password1',]
        labels = { 'Username':"Email", 'Password1':"Password"}
        
class SignUpForm(forms.ModelForm):
    username = forms.CharField(max_length=80)
    mob = forms.IntegerField()
    first_Name = forms.CharField(max_length=255)
    last_Name = forms.CharField(max_length=255)
    
    class Meta:
        model = U
        fields = ('username', 'password1', 'password2' ,'email', )
        labels = {'mob': 'Mobile Number','first':'First Name','last':'Last Name',}'''
        
'''class RegistrationForm(forms.ModelForm):
    name = forms.CharField(max_length=455,required=True)
    email = forms.EmailField(max_length=643,required=True,widget=forms.TextInput())
    password1 = forms.CharField(max_length=83, widget=forms.PasswordInput,required=True)
    Password = forms.CharField(max_length=83,widget=forms.PasswordInput,required=True)
    class Meta:
        model = registrationForm
        fields = ['email', 'password1','Password','name',]'''
''' Middle_Name = forms.CharField(max_length=445)
    Last_Name = forms.CharField(max_length=345)
    Mob = forms.IntegerField(max_length=14)
    Address = forms.CharField(max_length=877)
    Gender = forms.ModelFormOptions(Male='male',Female='female',other='other')'''
    
class CustomerRegistrationFrom(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus':'True'
                                                             ,'class' : 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'form-control'
    }))
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(
        attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
    
class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password',widget=forms.PasswordInput(
        attrs={'autofocus':'True','autocomplete':'current-password','class':'form-control'}
    ))
    new_password1 = forms.CharField(label='New Password',widget=forms.PasswordInput(
        attrs={"autocomplete":'current-password','class':'form-control'}))
    new_password2 = forms.CharField(label='New Password',widget=forms.PasswordInput(
        attrs={"autocomplete":'current-password','class':'form-control'}))
    
class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"class":'form-control'}))
    
class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label='New Password',widget=forms.PasswordInput(attrs=
                                                                                    {"autocomplete":'current-password','class' : 'form-control'}))
    new_password2 = forms.CharField(label='New Password',widget=forms.PasswordInput(attrs=
                                                                                    {"autocomplete":'current-password','class' : 'form-control'}))
class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name','locality','city','mobile','state','zipcode']
        widgets ={
            'name' : forms.TextInput(attrs={"class":"form-control"}),
            'locality' : forms.TextInput(attrs={"class":"form-control"}),
            'city' : forms.NumberInput(attrs={"class":"form-control"}),
            'mobile' : forms.NumberInput(attrs={"class":"form-control"}),
            'state' : forms.Select(attrs={"class":"form-control"}),
            'zipcode' : forms.NumberInput(attrs={"class":"forms-control"}),
        }
    
        
    
    