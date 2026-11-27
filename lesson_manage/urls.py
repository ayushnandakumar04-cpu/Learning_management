from django.urls import path
from lesson_manage.views import LessonCreateView,LessonRetrieveUpdateDeleteView
urlpatterns=[
    path('<int:pk>/module',LessonCreateView.as_view()),
    path('module/<int:pk>',LessonRetrieveUpdateDeleteView.as_view())
]