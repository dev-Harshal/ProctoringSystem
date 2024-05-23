from django.shortcuts import render,redirect
from ProctoringApp.models import *
from ProctoringApp.decorators import login_required_teacher
from ProctoringApp.tasks import update_status
# Create your views here.




@login_required_teacher()
def createExamView(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        Exam.objects.create(teacher=request.user,subject=subject, start_date=start_date,end_date=end_date, start_time=start_time, end_time=end_time)
        return redirect('list-exam')
    return render(request, 'create_exam.html')

@login_required_teacher()
def createQuestionView(request,exam_id):

    if request.method == 'POST':
        exam_id = request.POST.get('exam_id')
        question = request.POST.get('question')
        answer = request.POST.get('answer')
        marks = request.POST.get('marks')
        option_1 = request.POST.get('option_1')
        option_2 = request.POST.get('option_2')
        option_3 = request.POST.get('option_3')
        option_4 = request.POST.get('option_4')

        exam = Exam.objects.get(id=exam_id)

        Questions.objects.create(exam=exam,question=question,answer=answer,marks=marks,option1=option_1,option2=option_2,option3=option_3,option4=option_4)

        return redirect('list-exam')
    else:
        return render(request, 'create_question.html',context={'exam_id':exam_id})

@login_required_teacher()
def listExamView(request):
    update_status()
    exams = Exam.objects.filter(teacher=request.user).all()
    return render(request, 'list_exam.html',context={'exams':exams})


@login_required_teacher()
def updateExamView(request,exam_id):
    if request.method == 'POST':
        exam_id = request.POST.get('exam_id')
        subject = request.POST.get('subject')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        exam = Exam.objects.get(id=exam_id)
        exam.subject = subject
        exam.start_date = start_date
        exam.end_date = end_date
        exam.start_time = start_time    
        exam.end_time = end_time
        exam.save()
        return redirect('list-exam')
    else:
        exam = Exam.objects.get(id=exam_id)
        return render(request, 'update_exam.html',context={'exam':exam})

@login_required_teacher()
def listQuestionView(request,exam_id):
    exam = Exam.objects.get(id=exam_id)
    questions = Questions.objects.filter(exam=exam)
    total = sum([obj.marks for obj in questions])
    return render(request, 'list_question.html',context={'questions':questions,'exam':exam,'total':total})

@login_required_teacher()
def updateQuestionView(request,exam_id,question_id):
    if request.method == 'POST':
        exam = Exam.objects.get(id=exam_id)
        question_obj = Questions.objects.get(id=question_id)
        question = request.POST.get('question')
        answer = request.POST.get('answer')
        marks = request.POST.get('marks')
        option_1 = request.POST.get('option_1')
        option_2 = request.POST.get('option_2')
        option_3 = request.POST.get('option_3')
        option_4 = request.POST.get('option_4')
        question_obj.question = question
        question_obj.answer = answer
        question_obj.marks = marks
        question_obj.option1 = option_1
        question_obj.option2 = option_2
        question_obj.option3 = option_3
        question_obj.option4 = option_4
        question_obj.save()
        return redirect('/list_question/{}/'.format(question_obj.exam.id))

        
    else:
        question_obj = Questions.objects.get(id=question_id)
        return render(request, 'update_question.html',context={'exam_id':exam_id, 'question_id':question_id,'question_obj':question_obj})