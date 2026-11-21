from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import authentication,permissions
from course_manage.serializers import CourseSerializer
from course_manage.models import Course
from course_manage.permissions import IsOwner
class CourseListCreateview(ListCreateAPIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAdminUser]

    serializer_class=CourseSerializer
    queryset=Course.objects.all()

    def perform_create(self, serializer):
        serializer.save(trainer=self.request.user)

class CourseRetrieveUpdateview(RetrieveUpdateDestroyAPIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[IsOwner]

    serializer_class=CourseSerializer
    queryset=Course.objects.all()

  
