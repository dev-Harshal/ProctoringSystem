from django.urls import path
from ProctoringApp.views import *


urlpatterns = [
    
    path('create_exam/',createExamView,name="create-exam"),
    path('create_question/<int:exam_id>/',createQuestionView,name="create-question"),
    path('list_question/<int:exam_id>/',listQuestionView,name="list-question"),
    path('update_question/<int:exam_id>/<int:question_id>',updateQuestionView,name="update-question"),
    path('list_exam/',listExamView,name="list-exam"),
    path('update_exam/<int:exam_id>/',updateExamView,name="update-exam"),
]
