from rest_framework import serializers
from course_manage.models import Course
from module_manage.models import Module
from module_manage.serializers import ModuleSerializer
class CourseSerializer(serializers.ModelSerializer):
    modules = serializers.SerializerMethodField( read_only=True)
    total_modules=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Course

        fields="__all__"

        read_only_fields=["id","created_at","updated_at","trainer"]

    def get_modules(sel,obj):
        module_obj=Module.objects.filter(course=obj)
        serializer_instance=ModuleSerializer(module_obj,many=True)
        return serializer_instance.data
    def get_total_modules(self,obj):
        return obj.modules.count()
