from django import forms



class UpdateUsername(forms.Form):
    new_username = forms.CharField(max_length=100, required=True, label='New Username')
    confirm_new_username = forms.CharField(max_length=100, required=True, label='Confirm New Username')
    password = forms.CharField(max_length=100, required=True, label='Password', widget=forms.PasswordInput)

class UpdatePassword(forms.Form):
    current_password = forms.CharField(max_length=100, required=True, label='Password', widget=forms.PasswordInput)
    new_password = forms.CharField(max_length=100, required=True, label='New Password', widget=forms.PasswordInput)
    confirm_new_password = forms.CharField(max_length=100, required=True, label='Confirm New Password', widget=forms.PasswordInput)
