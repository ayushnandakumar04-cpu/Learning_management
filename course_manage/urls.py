from django.urls import path
from course_manage.views import CourseListCreateview,CourseRetrieveUpdateview
urlpatterns=[
    path('list/',CourseListCreateview.as_view()),
    path('update/<int:pk>/',CourseRetrieveUpdateview.as_view()),
]