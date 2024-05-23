from django.urls import path
from ProctoringApp.views import *


urlpatterns = [
    
    path('create_exam/',createExamView,name="create-exam"),
    path('create_question/<slug:exam_id>/',createQuestionView,name="create-question"),
    path('list_question/<slug:exam_id>/',listQuestionView,name="list-question"),
    path('update_question/<slug:exam_id>/<int:question_id>',updateQuestionView,name="update-question"),
    path('list_exam/',listExamView,name="list-exam"),
    path('update_exam/<slug:exam_id>/',updateExamView,name="update-exam"),
]
