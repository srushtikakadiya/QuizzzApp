from django.urls import path
from .views import uploadFileView,add_quiz, questions, deletequiz, update_question, openquiz, viewquizplaceholder


urlpatterns = [
    path('upload', uploadFileView, name="UploadView"),
    path('quiz', add_quiz, name="add_quiz"),
    path('question/', questions, name="questions_data"),
    path("deletequiz/", deletequiz, name="delete_quiz"),
    path("openquiz/<id>/", openquiz, name="openquiz"),
    path("updatequestion/<id>/", update_question, name="update_quiz"),
    path("viewquizplaceholder/<id>/", viewquizplaceholder, name="viewquizplaceholder"),
]