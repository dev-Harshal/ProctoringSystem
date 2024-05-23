from django.urls import path
from Examination.views import *


urlpatterns = [
    path('student_list_exam/',listExamStudentView,name='student-list-exam')
]
