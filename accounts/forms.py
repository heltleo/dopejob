from django import forms
from accounts.models import User
from accounts.models import Student
from accounts.models import Employee


class EmployeeProfileForm(forms.ModelForm):

    class Meta:
        model = Employee
        exclude = ('friends',)

class StudentProfileForm(forms.ModelForm):

    class Meta:
        model = Student
        exclude = ('friends',)



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
