from django.shortcuts import render,redirect
from ProctoringApp.models import *
from datetime import datetime, date, time
from ProctoringApp.tasks import update_status
# Create your views here.


def listExamStudentView(request):
    update_status()
    exams = Exam.objects.all()
    return render(request, 'Examination/student_list_exam.html',context={'exams':exams})

def listQuestionStudentView(request,exam_id):
    if request.method == 'POST':
        id = request.POST.get('id')
        mcq = request.POST.get('mcq')
        obj = Questions.objects.get(id=id)
        if mcq == obj.answer:
            if Result.objects.filter(student=request.user,exam=obj.exam).exists():
                obj1 = Result.objects.get(student=request.user,exam=obj.exam)
                obj1.score = obj1.score + obj.marks
                obj1.save()
            else:
                Result.objects.create(student=request.user,exam=obj.exam,score=obj.marks)
        else:
            pass
        return redirect('/student_question_exam/{}'.format(obj.exam.id))
                



        
    else:
        exam = Exam.objects.get(id=exam_id)
        questions = set(Questions.objects.filter(exam=exam).all())
        return render(request, 'Examination/student_list_question.html', context={'questions':list(questions)})