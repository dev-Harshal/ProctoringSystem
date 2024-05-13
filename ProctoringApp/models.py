from django.db import models
from Users.models import User
# Create your models here.


class Exam(models.Model):
    teacher = models.ForeignKey(User,on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(max_length=10,choices=(('Active','Active'),('Completed','Completed')),default="Active")

class Questions(models.Model):
    exam = models.ForeignKey(Exam,on_delete=models.CASCADE)
    question = models.CharField(max_length=1000)
    option1 = models.CharField(max_length=1000)
    option2 = models.CharField(max_length=1000)
    option3 = models.CharField(max_length=1000)
    option4 = models.CharField(max_length=1000)
    answer = models.CharField(max_length=1000)
    marks = models.IntegerField()