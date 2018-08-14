from django.shortcuts import render, redirect
from accounts.models import User
from accounts.forms import StudentProfileForm
from accounts.forms import EmployeeProfileForm
from accounts.forms import LoginForm

# Create your views here.
def login(request):
    if len(request.POST) > 0:
        form = LoginForm(request.POST)
        if form.is_valid():
            user_mail = form.cleaned_data['email']
            logged_user = User.objects.get(email=user_mail)
            request.session['logged_user_id'] = logged_user.id
            return redirect('/')
        else:
            return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

def logout(request):
    pass

def register(request):
    if len(request.GET) > 0 and 'profileType' in request.GET:
        employeeForm = EmployeeProfileForm(prefix="em")
        studentForm = StudentProfileForm(prefix="st")
        if request.GET['profileType'] == 'student':
            studentForm = StudentProfileForm(request.GET, prefix="st")
            if studentForm.is_valid():
                studentForm.save()
                return redirect('/login')
        elif request.GET['profileType'] == 'employee':
            employeeForm = EmployeeProfileForm(request.GET, prefix="em")
            if employeeForm.is_valid():
                employeeForm.save()
                return redirect('/login')
        return render(request, 'user_profile.html', {'studentForm': studentForm, 'employeeForm': employeeForm})
    else:
        studentForm = StudentProfileForm(prefix="st")
        employeeForm = EmployeeProfileForm(prefix="em")
        return render(request, 'user_profile.html', {'studentForm': studentForm, 'employeeForm': employeeForm})
