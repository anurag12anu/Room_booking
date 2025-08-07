from django import forms
from .Model.Auth_Model.auth import Auth_user
from hotel_app.Model.Hotel_Model.customer import Customer

class Register_form(forms.ModelForm):
    class Meta:
        model=Auth_user
        fields = '__all__'
        
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter Email'}),
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Enter Password', 
                'autocomplete': 'new-password'  # prevents autofill
            }),
        }


class Login_form(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter Password',
            'autocomplete': 'new-password'
        })
    )
    
    
class Booking_Form(forms.ModelForm):
    check_in =forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    check_out=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
        
    class Meta:
        model=Customer
        fields=['name','email','phone','check_in','check_out']    
