from django.shortcuts import render
from ProctoringApp.models import Exam
from datetime import datetime, date, time
from ProctoringApp.tasks import update_status
# Create your views here.


def listExamStudentView(request):
    update_status()
    exams = Exam.objects.all()
    return render(request, 'Examination/list_exam.html',context={'exams':exams})