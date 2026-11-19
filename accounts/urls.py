
from django.urls import path
from accounts.views import RegisterStudentView,RegisterTrainerView,TrainerProfileUpdateView,GetTrainerProfileView,StudentProfileUpdateView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import TokenRefreshView,TokenObtainPairView
urlpatterns = [
    path('student/register',RegisterStudentView.as_view()),
    path('student/jwt/login',TokenObtainPairView.as_view()),
    path('student/jwt/refresh/login',TokenRefreshView.as_view()),
    path('student/profile',StudentProfileUpdateView.as_view()),

    path('trainer/register',RegisterTrainerView.as_view()),
    path('trainer/login',ObtainAuthToken.as_view()),
    path('trainer/profile',TrainerProfileUpdateView.as_view()),
    path('trainer/me',GetTrainerProfileView.as_view())
]