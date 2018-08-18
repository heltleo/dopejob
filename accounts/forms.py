from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from accounts.models import User
from accounts.models import Student
from accounts.models import Employee
from accounts.models import Enterprise
from accounts.models import Message

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2


class UserAdminCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'active', 'admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class EnterpriseProfileForm(RegisterForm):
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)

    class Meta:
        model = Enterprise
        exclude = ('friends', 'active', 'staff', 'admin', 'last_login',)


class EmployeeProfileForm(RegisterForm):
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)

    class Meta:
        model = Employee
        exclude = ('friends', 'active', 'staff', 'admin', 'last_login',)


class StudentProfileForm(RegisterForm):
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)

    class Meta:
        model = Student
        exclude = ('friends', 'active', 'staff', 'admin', 'last_login',)



class LoginForm(forms.Form):
    email = forms.EmailField(label='Courriel')
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            result = User.objects.filter(password=password, email=email)

            if len(result) != 1:
                raise forms.ValidationError("Adresse de courriel ou mot de passe erroné(e).")

        return cleaned_data


class MessageForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Please enter the message'}))

    class Meta:
        model = Message
        fields = (
            'author',
            'topic',
            'content',
        )
