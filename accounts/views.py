from django.shortcuts import render, redirect
from accounts.forms import StudentProfileForm
from accounts.forms import EmployeeProfileForm

# Create your views here.
def login(request):
    pass

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
