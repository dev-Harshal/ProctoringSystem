import uuid
from django.db import models
from Users.models import User
# Create your models here.


class Exam(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    teacher = models.ForeignKey(User,on_delete=models.CASCADE)
    subject = models.CharField(max_length=100,null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    status = models.CharField(max_length=10,choices=(('Active','Active'),('In Active','In Active'),('Completed','Completed')),default="In Active")

    

class Questions(models.Model):
    exam = models.ForeignKey(Exam,on_delete=models.CASCADE)
    question = models.CharField(max_length=100,null=True, blank=True)
    option1 = models.CharField(max_length=100,null=True, blank=True)
    option2 = models.CharField(max_length=100,null=True, blank=True)
    option3 = models.CharField(max_length=100,null=True, blank=True)
    option4 = models.CharField(max_length=100,null=True, blank=True)
    answer = models.CharField(max_length=100,null=True, blank=True)
    marks = models.IntegerField(null=True, blank=True)


class Result(models.Model):
    exam = models.ForeignKey(Exam,on_delete=models.CASCADE)
    student = models.ForeignKey(User,on_delete=models.CASCADE)
    score = models.IntegerField(null=True, blank=True,default=0)
    total = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=10,choices=(('Active','Active'),('Completed','Completed')),default="Active")

