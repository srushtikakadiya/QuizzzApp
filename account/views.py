from django.http import request, response
from django.http import JsonResponse
from django.shortcuts import redirect, render 
from django.contrib.auth.models import User,Permission
from django.contrib.contenttypes.models import ContentType
from question.models import Question, Quiz, UserResult
from django.contrib.auth import authenticate, login, logout
import random

# Create your views here.
def home(request):
    return render(request, 'home.html')

def logout_user(request):
    logout(request)
    return render(request, 'home.html')

def staff_panel(request):
    return render(request, 'staffpanel.html')

def student_panel(request):
    return render(request, "studentpanel.html")


def f_register(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == "POST":
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            email = request.POST['email']
            user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
            user.is_staff=True    
            
            content_type = ContentType.objects.get_for_model(Question)
            permission = Permission.objects.get( codename='change_question',
            content_type=content_type, ) 
            user.user_permissions.add(permission)

            #add
            permission1 = Permission.objects.get( codename='add_question',
            content_type=content_type, ) 
            user.user_permissions.add(permission1)

            user.save()
            print (user.has_perm('Question.add_question'))
            print (user.has_perm('Question.change_question'))
            print("user created")
            return redirect("/")
        else:
            print("user Not created")
    return render(request,'faculty_reg.html')

def f_login(request):

    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':

            username = request.POST['username']
            password = request.POST['password1']
            
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_staff:
                    login(request, user)
                    print("login sucess")
                    return redirect('/staffpanel') 
                else:
                    print("not a staff")
                    return render(request, 'faculty_login.html')
            else:
                print("login fail")
                redirect('/')
    return render(request, 'faculty_login.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == "POST":
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            email = request.POST['email']
            user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
            user.save()
            print("user created")
            return redirect("/")
        else:
            print("user Not created")
    return render(request,'register.html')

def login_user(request):

    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password1']
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                if user.is_staff:
                    login(request, user)
                    print("login sucess")
                    return redirect('/staffpanel')
                else:
                    login(request, user)
                    print("login sucess")
                    return redirect('/studentpanel')
            else:
                print("login fail")
                redirect('/')
    return render(request, 'login.html')

def view_quiz_data(request):
    userresult = UserResult.objects.all()
    quizname = Quiz.objects.filter()
    
    return render(request, "checkquiz.html",{"quizes":quizname,"resultquizes":userresult})


def viewquiz(request, id):
    questions = Question.objects.filter(quiz_name=id)
    length = len(questions)
    question = questions.first()
    quiz=Quiz.objects.get(id=id)
    res = UserResult.objects.filter(username=request.user,quiz_name=quiz).first()
    if res is None:
        res = UserResult(username=request.user, quiz_name=quiz)
        res.save()
        
    if request.method == "POST":
        time = request.POST["startdate"]
        if(time != 00):
            qid = int(request.POST["number"])-1
            question = questions[qid]
            rightans = question.correctAns
            if(rightans.strip() == request.POST["option"].strip()):
                print("correct")
                res.score=res.score+1
                res.save() 
            else:
                print("wrong")
        else:
            return redirect("/showresult")

        if len(questions) == qid+1:
            return redirect("/showresult")
        else:
            question = questions[qid+1]
            data = {
                "number":int(request.POST["number"])+1,
                "questions":question.question,
                "optionA":question.optionA,
                "optionB":question.optionB,
                "optionC":question.optionC,
                "optionD":question.optionD,
                "ques_id":question.id,
            }
            return JsonResponse(data)
    return render(request, "choosequiz.html", {"question":question ,"number":1, "totalqs":len(questions), "time_quiz":length })


def showResult(request):
    userresult = UserResult.objects.filter(username=request.user)
    return render(request,"showresult.html",{"userresult":userresult})

def displayResult(request):
    dispuserresult = UserResult.objects.filter(username=request.user)
    return render(request,"showresult.html",{"userresult":dispuserresult})