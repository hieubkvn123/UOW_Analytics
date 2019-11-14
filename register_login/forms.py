from django import forms

text_input = forms.TextInput(attrs = {'class' : 'form-control'})
password_input = forms.TextInput(attrs = {'class' : 'form-control', 'type' : 'password'})

class Register(forms.Form):
    first_name = forms.CharField(label = 'First Name', max_length = 200, widget = text_input)
    last_name = forms.CharField(label = 'Last Name', max_length = 200, widget = text_input)
    major = forms.CharField(label = 'Major', max_length = 200, widget = text_input)
    faculty = forms.CharField(label = 'Faculty', max_length = 200, widget = text_input)
    username = forms.CharField(label = 'Username', max_length = 200, widget = text_input)
    password = forms.CharField(label = 'Password', max_length = 200, widget = password_input)

class Login(forms.Form):
    username = forms.CharField(label = 'Username', max_length = 200, widget = text_input)
    password = forms.CharField(label = 'Password', max_length = 200, widget = password_input)
 
