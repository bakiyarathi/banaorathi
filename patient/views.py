from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if user.user_type == 1:
                return redirect('patient_dashboard')
            elif user.user_type == 2:
                return redirect('doctor_dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, '/home/rathi/internship/internproject/patient/templates/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.user_type == 1:
                return redirect('patient_dashboard')
            elif user.user_type == 2:
                return redirect('doctor_dashboard')
        else:
            return render(request, '/home/rathi/internship/internproject/patient/templates/login.html', {'error': 'Invalid credentials'})
    return render(request, '/home/rathi/internship/internproject/patient/templates/login.html')

@login_required
def patient_dashboard(request):
    return render(request, '/home/rathi/internship/internproject/patient/templates/patient_dashboard.html',{'user': request.user})

@login_required
def doctor_dashboard(request):
    return render(request, '/home/rathi/internship/internproject/patient/templates/doctor_dashboard.html', {'user': request.user})


