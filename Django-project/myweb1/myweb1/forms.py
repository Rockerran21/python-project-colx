from django import forms # Import the forms module from Django
class UserForm(forms.Form):  # Create a form class
    num1 = forms.CharField(required=False)  # Create a form field
    num2 = forms.CharField(required=False)  # Create a form field
    #Define More Fields as needed