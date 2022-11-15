from django.contrib.auth.models import User
from django.core.checks import messages
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import Question, Quiz
# Create your views here. 

def viewquizplaceholder(request,id):
    quiz = Quiz.objects.filter(id=id)
    question = Question.objects.all()
    length = len(question)
    print("dsfadfsdg",length)
    if request.method=="POST":
        quiz = Quiz.objects.get(id=id)
        i = quiz.id
        return redirect(f"/viewquiz/{quiz.id}/")

    return render(request,"quizplaceholder.html",{"quizes":quiz,"length":length })

#add quiz
def add_quiz(request):
    quiz = Quiz.objects.all()
    message = ""
    if request.method=="POST":
        quiz_name=request.POST["quiz_name"]
        quiz_marks=request.POST["quiz_marks"]
        if Quiz.objects.filter(quiz_name=quiz_name).exists():
            print("Quiz already exists")
            message = "Quiz already exists"
        else:
            quiz = Quiz(quiz_name=quiz_name,quiz_marks=quiz_marks,user=request.user)        
            quiz.save()
            return redirect("UploadView")        
    return render(request,"add_quiz.html",{"message":message})

def uploadFileView(request):
    q=Quiz.objects.filter(user=request.user)
    if request.method == "POST":    
        uploadFile = request.FILES['myfile']
        data_set = uploadFile.read().decode("utf-8").strip()
        name=request.POST["quizess"]
        qq = Quiz.objects.filter(id=name).first()
        for row in data_set.split("\n")[1:]:
            cols = row.split(",")
            question = Question(question=cols[0],optionA=cols[1],optionB=cols[2],optionC=cols[3],optionD=cols[4],correctAns=cols[5],quiz_name=qq,user=request.user)
            question.save()
        print("current logged in user is ",request.user)
        if request.user.is_anonymous:
            redirect("/log")
        else:
            if Question.objects.filter(user=request.user):
                if Question.objects.all() is None:
                    question = "nothing to show"
                    return render(request, 'upload.html', {"question":question})
                else:
                    return redirect("/question")
            else:
                questions = "u r not authenticated"
                redirect("/log")
    return render(request, 'upload.html', {"q":q} )

def questions(request):
    quiz = Quiz.objects.filter(user=request.user)
    count = Quiz.objects.filter(user=request.user).count()
    if count <= 0:
        return redirect('/quiz')
    else:
        if request.method == "POST":
            id = request.POST["quizess"]
            if request.user.is_anonymous:
                redirect("/log")
            else:
                if Question.objects.filter(user=request.user):
                    if Question.objects.all() is None:
                        message = "nothing to show"
                    questions = Question.objects.filter(user=request.user,quiz_name=id)
                    return render(request, 'question.html', {"quiz":quiz,"questions":questions})
                else:
                    question = "u r not authenticated"
                    print(question)
                    redirect("/log")
    return render(request, "question.html",{"quiz":quiz})


def openquiz(request, id):
    questions = Question.objects.filter(quiz_name=id)
    question = questions.first()
    quiz=Quiz.objects.get(id=id)
    if request.method == "POST":        
        qid = int(request.POST["number"])-1
        question = questions[qid]
        question = questions[qid+1]
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
    return render(request, "choosequiztoupdate.html",{"question":question,"number":1,"totalqs":len(questions)})

    # res = UserResult.objects.filter(username=request.user,quiz_name=quiz).first()
    # if res is None:
    #     res = UserResult(username=request.user,quiz_name=quiz)
    #     res.save()
    


def update_question(request,id):
    quiz = Quiz.objects.filter(user = request.user)
    question = Question.objects.filter(id=id)
    if request.method == "POST":
        question = Question.objects.get(id=id)
        question.question = request.POST["question"]
        question.optionA = request.POST["optionA"]
        question.optionB = request.POST["optionB"]
        question.optionC = request.POST["optionC"]
        question.optionD = request.POST["optionD"]
        question.correctAns = request.POST["ans"]
        question.save()
        return redirect("/question")       
    return render(request, "updatequestion.html",{"question":question})
    

def deletequiz(request):
    quizname = Quiz.objects.filter(user=request.user)
    if quizname.exists():
        if request.method == "POST":
            name = request.POST["deletequiz"]
            if name is None:
                print("not found")
            else:
                Quiz.objects.filter(user=request.user, quiz_name=name).delete()
                print("quiz is deleted")
    else:
        print("Quiz is not added")
        redirect('/quiz')
    return render(request, "deletequiz.html",{"quiznames":quizname})