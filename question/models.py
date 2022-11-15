from typing import Tuple
from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
# Create your models here.

# Quiz model
class Quiz(models.Model):
    quiz_name = models.CharField(max_length=500)
    quiz_marks = models.IntegerField()    
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=True)

    def __str__(self):
        return self.quiz_name
 
class Question(models.Model):
    question = models.CharField(max_length=500)
    optionA = models.CharField(max_length=500)
    optionB = models.CharField(max_length=500)
    optionC = models.CharField(max_length=500)
    optionD = models.CharField(max_length=500) 
    correctAns =  models.CharField(max_length=500,default="")
    quiz_name = models.ForeignKey(Quiz, on_delete=models.CASCADE,default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=True)

    def __str__(self):
        return self.question

class UserResult(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE,default=True)
    score = models.IntegerField(default=0)
    quiz_name = models.ForeignKey(Quiz, on_delete=models.CASCADE,default=True)
    
    def __str__(self):
        return str(self.quiz_name)