from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate
from accounts.models import User
from accounts.forms import StudentProfileForm
from accounts.forms import EmployeeProfileForm
from accounts.forms import EnterpriseProfileForm
from accounts.forms import LoginForm

# Create your views here.
def login_view(request):
    if len(request.POST) > 0:
        form = LoginForm(request.POST)
        if form.is_valid():
            return redirect('/')
        else:
            return render(request, 'login.html', {'form': form})
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
        return render(request, 'user_profile.html', {'studentForm': studentForm, 'employeeForm': employeeForm, 'enterpriseForm': enterpriseForm})
    else:
        studentForm = StudentProfileForm(prefix="st")
        employeeForm = EmployeeProfileForm(prefix="em")
        enterpriseForm = EnterpriseProfileForm(prefix="en")
        return render(request, 'user_profile.html', {'studentForm': studentForm, 'employeeForm': employeeForm, 'enterpriseForm': enterpriseForm})
