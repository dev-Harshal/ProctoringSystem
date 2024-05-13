from django.urls import path
from Users.views import *


urlpatterns = [
    path('',indexView,name='index'),
    path('register/',registerView,name='register'),
    path('login/',loginView,name='login'),
    path('logout/',logoutView,name='logout'),
    path('verify_otp/',verifyOTPView,name='verify-otp'),
    path('student_dashboard/',studentDashboardView,name='student-dashboard'),
    path('teacher_dashboard/',teacherDashboardView,name='teacher-dashboard'),
]
