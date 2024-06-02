from django.shortcuts import render,redirect
from Users.models import User,OTP  
from django.contrib.auth import authenticate,login,logout
import random
from Users.mail import send_mail_to_the_user
from ProctoringApp.decorators import login_required_teacher
# Create your views here.

def indexView(request):
    return render(request, 'index.html')

def studentDashboardView(request):
    return render(request, 'student_dashboard.html')

@login_required_teacher()
def teacherDashboardView(request):
    return render(request, 'teacher_dashboard.html')


def registerView(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        role =request.POST.get('role')
        photo = request.FILES.get('photo')
        if User.objects.filter(email=str(email).lower()).exists():
            return render(request,'register.html')
        User.objects.create(full_name=str(full_name).title(),email=str(email).lower(),password=password,photo=photo,username=email,role=role)
        return redirect('index')
    else:
        return render(request, 'register.html')
    

def loginView(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        role =request.POST.get('role')
        user = authenticate(email=email, password=password)
        if user is not None and role==user.role:
            otp = str(random.randint(1000, 9999))
            if OTP.objects.filter(user=user).exists():
                obj = OTP.objects.filter(user=user).last()
                obj.otp = otp
                obj.save()
                print("OTP:",otp)
                send_mail_to_the_user(email,otp)
                return redirect('/verify_otp/?email=' + email)
            else:
                OTP.objects.create(user=user, otp=otp)
                print("OTP:",otp)
                send_mail_to_the_user(email,otp)
                return redirect('/verify_otp/?email=' + email)
        else:
            return render(request,'login.html')        
    else:
        return render(request, 'login.html')
    

def verifyOTPView(request):
    if request.method == 'POST':
        email = request.GET.get('email')
        otp = request.POST.get('otp')
        try:
            user = User.objects.get(email=email)
            obj = OTP.objects.filter(user=user).last()
        except:
            return render(request,'verify_otp.html',{'email':email})
        if obj.otp == otp:
            obj.otp = ""
            obj.save()
            login(request,user)
            return redirect('{}-dashboard'.format(str(user.role).lower()))
        else:
            return render(request,'verify_otp.html',{'email':user.email})
    else:
        return render(request,'verify_otp.html')
    

def logoutView(request):
    logout(request)
    return redirect('index')