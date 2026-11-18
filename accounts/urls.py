
from django.urls import path
from accounts.views import CreateStudentView,CreateTrainerView
urlpatterns = [
    path('student/register',CreateStudentView.as_view()),
    path('trainer/register',CreateTrainerView.as_view())
]