from django.shortcuts import render,get_object_or_404
from rest_framework import authentication,permissions
from lesson_manage.permissions import IsTrainer
from rest_framework.views import APIView
from lesson_manage.serializers import LessonSerializer
from module_manage.models import Module
from lesson_manage.models import Lessons
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView
# Create your views here.

class LessonCreateView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsTrainer]
    def post(self,request,pk=None):
        module_id=pk
        form_data=request.data
        module_obj=get_object_or_404(Module,id=module_id)
        seializer_instance=LessonSerializer(data=form_data)
        if seializer_instance.is_valid():
            seializer_instance.save(module=module_obj,trainer=request.user)
            return Response(data=seializer_instance.data)
        else:
            return Response(data=seializer_instance.errors)

class LessonRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsTrainer]
    serializer_class=LessonSerializer
    queryset=Lessons.objects.all()