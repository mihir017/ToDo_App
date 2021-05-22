from django.urls import path, include
from . import views
urlpatterns = [
    path("",views.mainPage,name="mainPage"),
    # path("signUp/",views.signUp,name="signUp"),
    path("createAccount/",views.createAccount,name="createAccount"),
    path("logIn/",views.logIn,name="logIn"),
    path("logout/",views.logOut,name="logOut"),
    path("home/",views.homePage,name="homePage"),
    path("addTask/",views.addTask,name="addTask"),
    path("completeTask/<str:pk>/",views.completeTask,name="completeTask"),
    path("deleteTask/<str:pk>/",views.deleteTask,name="deleteTask"),
]
