from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignIn, SignUp, Task_form
from .models import User, Task

# Create your views here.

def mainPage(request):
    if request.session.get("is_login"):
        return redirect('homePage')
    else:
        signin_form = SignIn()
        signup_form = SignUp()
        context = {"signin_form":signin_form,"signup_form":signup_form}
        return render(request,"form.html",context)

# def signUp(request):
#     if request.session.get('is_login'):
#         return redirect('homePage')
#     else:
#         form = SignUp()
#         context = {"form":form}
#         return render(request,"signup.html",context)

def logOut(request):
    del request.session['email']
    # del request.session['is_login']
    request.session['is_login'] = False
    return redirect("mainPage")

def createAccount(request):
    if request.method == "POST":
        form = SignUp(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            pass1 = form.cleaned_data.get("password")
            pass2 = form.cleaned_data.get("re_password")
            if len(pass1) >= 6:
                if pass1 == pass2:
                    User.objects.create(username = username, email = email, password = pass1)
                    return redirect("mainPage")
                else:
                    return HttpResponse("Password Doesn't match")
            else:
                return HttpResponse("Min lenght of password is 6 character")
        else:
            return HttpResponse("form is not valid")

def logIn(request):
    if request.method == 'POST':
        login_form = SignIn(request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data.get("email")
            password = login_form.cleaned_data.get("password")
            try:
                User.objects.get(email = email)
            except Exception as err:
                return HttpResponse("Email is not register")
            else:
                user = User.objects.get(email = email)
                if user.password == password:
                    request.session['email'] = email
                    request.session['is_login'] = True
                    return redirect("homePage")
                else:
                    return HttpResponse("Email or password is wrong")
        else:
            return HttpResponse("Form is not valid")
            
def completeTask(request,pk):
    task = Task.objects.get(id = pk)
    task.complete = True
    task.save()
    return redirect("homePage")

def deleteTask(request,pk):
    task = Task.objects.get(id = pk)
    task.delete()
    return redirect("homePage")

def homePage(request):
    task_form = Task_form()
    user_email = User.objects.get(email = request.session.get("email"))
    user_Task = Task.objects.filter(user = user_email)
    # print(user_Task)
    context = {"form": task_form,"all_task": user_Task,"user":user_email}
    return render(request,"index.html",context)

def addTask(request):
    if request.method == 'POST':
        form = Task_form(request.POST)
        print(form)
        if form.is_valid():
            # form.user = request.session.get("email")
            # form.save()
            data = {
                "user" : User.objects.get(email = request.session.get('email')),
                "task" : form.cleaned_data.get("task"),
            }
            Task.objects.create(**data)
            return redirect("homePage")
        # else:
        #     return HttpResponse("Form is not valid")