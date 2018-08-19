from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, authenticate, login
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from accounts.models import User
from accounts.forms import StudentProfileForm
from accounts.forms import EmployeeProfileForm
from accounts.forms import EnterpriseProfileForm
from accounts.forms import LoginForm

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['email']
            p = form.cleaned_data['password']
            user = authenticate(email=u, password=p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
                else:
                    messages.add_message(
                        request, messages.INFO, _('Ce compte a été désactiver.')
                    )
            else:
                messages.add_message(
                    request, messages.ERROR, _('L\'email ou le mot de passe est erroné.')
                )
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/accounts/login')

def register_view(request):
    if len(request.GET) > 0 and 'profileType' in request.GET:
        employeeForm = EmployeeProfileForm(prefix="em")
        studentForm = StudentProfileForm(prefix="st")
        if request.GET['profileType'] == 'student':
            studentForm = StudentProfileForm(request.GET, prefix="st")
            if studentForm.is_valid():
                studentForm.save()
                return redirect('/accounts/login')
        elif request.GET['profileType'] == 'employee':
            employeeForm = EmployeeProfileForm(request.GET, prefix="em")
            if employeeForm.is_valid():
                employeeForm.save()
                return redirect('/accounts/login')
        elif request.GET['profileType'] == 'enterprise':
            enterpriseForm = EnterpriseProfileForm(request.GET, prefix="en")
            if enterpriseForm.is_valid():
                enterpriseForm.save()
                return redirect('/accounts/login')
        return render(request, 'register.html', {'studentForm': studentForm, 'employeeForm': employeeForm, 'enterpriseForm': enterpriseForm})
    else:
        studentForm = StudentProfileForm(prefix="st")
        employeeForm = EmployeeProfileForm(prefix="em")
        enterpriseForm = EnterpriseProfileForm(prefix="en")
        return render(request, 'register.html', {'studentForm': studentForm, 'employeeForm': employeeForm, 'enterpriseForm': enterpriseForm})


@login_required
def profile(request):
    return render(request, 'user_profile.html', {})
