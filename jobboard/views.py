from django.shortcuts import render, redirect
from accounts.models import User
from accounts.models import Student
from accounts.models import Employee

# Create your views here.
def get_logged_user_from_request(request):
    if 'logged_user_id' in request.session:
        logged_user_id = request.session['logged_user_id']
        if len(Student.objects.filter(id=logged_user_id)) == 1:
            return Student.objects.get(id=logged_user_id)
        elif len(Employee.objects.filter(id=logged_user_id)) == 1:
            return Employee.objects.get(id=logged_user_id)
        else:
            return None
    else:
        return None

def index(request):
    logged_user = get_logged_user_from_request(request)
    
    if logged_user:
        return render(request, 'index.html', {'logged_user': logged_user})
    else:
        return render(request, 'index.html')
