from django.urls import path
from lesson_manage.views import LessonCreateView
urlpatterns=[
    path('<int:pk>/module',LessonCreateView.as_view())
]