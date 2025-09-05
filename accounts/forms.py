from django import forms
from .models import MongoUser

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        u = self.cleaned_data.get("username").strip()
        if MongoUser.objects(username=u).first():
            raise forms.ValidationError("Username already exists")
        return u

    def clean_email(self):
        e = self.cleaned_data["email"].strip().lower()
        if MongoUser.objects(email=e).first():
            raise forms.ValidationError("Email already registered")
        return e

    def clean(self):
        cleaned = super().clean()
        p1, p2 = cleaned.get("password1"), cleaned.get("password2")
        if p1 and p2 and p1 != p2:
            self.add_error("password2", "Passwords do not match")
        return cleaned

    
class LoginForm(forms.Form):
    # accept either username OR email in the same field
    login = forms.CharField(label="Username or Email")
    password = forms.CharField(widget=forms.PasswordInput)