from os import name

from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('reg/', views.register, name="reg"),
    path('log/', views.login_user, name="log"),
    path('logout/', views.logout_user, name="logout"),
    path('freg/', views.f_register, name="freg"),
    path('flog/', views.f_login, name="flog"),
    path('staffpanel/',views.staff_panel, name="navigate_tostaffpanel"),
    path("studentpanel/", views.student_panel, name="navigate_tostudentpanel"),
    path('choosequiz/', views.view_quiz_data, name="choosequiz"),
    path('viewquiz/<id>/', views.viewquiz, name="quizview"),
    path('showresult/', views.showResult, name="resultViews"),
    path('displayresult/', views.displayResult, name="displayresultViews")
]