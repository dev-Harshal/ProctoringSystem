from django.urls import path
from Examination.views import *


urlpatterns = [
    path('student_list_exam/',listExamStudentView,name='student-list-exam'),
    path('student_question_exam/<slug:exam_id>',listQuestionStudentView,name='student-list-question'),
]
