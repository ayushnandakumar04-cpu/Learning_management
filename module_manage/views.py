from django.shortcuts import render,get_object_or_404
from rest_framework import authentication,permissions
from rest_framework.views import APIView
from module_manage.serializers import ModuleSerializer
from course_manage.models import Course
from module_manage.models import Module
from rest_framework.response import Response
# Create your views here.

class ModuleCreateView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]
    def post(self,request,pk=None):
        form_data=request.data
        course_id=pk
        course_obj=get_object_or_404(Course,id=course_id)
        seializer_instance=ModuleSerializer(data=form_data)
        if seializer_instance.is_valid():
            seializer_instance.save(course=course_obj,trainer=request.user)
            return Response(data=seializer_instance.data)
        else:
            return Response(data=seializer_instance.errors)
        