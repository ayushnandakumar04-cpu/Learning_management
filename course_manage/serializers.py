from rest_framework import serializers
from course_manage.models import Course
from module_manage.models import Module
from module_manage.serializers import ModuleSerializer
class CourseSerializer(serializers.ModelSerializer):
    modules = ModuleSerializer(many=True, read_only=True)
    class Meta:
        model=Course

        fields="__all__"

        read_only_fields=["id","created_at","updated_at","trainer"]

       
