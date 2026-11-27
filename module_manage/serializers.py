from rest_framework import serializers
from module_manage.models import Module
from lesson_manage.models import Lessons
from lesson_manage.serializers import LessonSerializer
class ModuleSerializer(serializers.ModelSerializer):

    lessons=serializers.SerializerMethodField(read_only=True)
    lesson_count=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Module
        fields="__all__"
        read_only_fields=["id","created_at","updated_at","course","trainer","module_number"]

    def get_lessons(sel,obj):
            module_obj=Lessons.objects.filter(module=obj)
            serializer_instance=LessonSerializer(module_obj,many=True)
            return serializer_instance.data
    def get_lesson_count(self,obj):
            return obj.lessons.count()
    
    # def course_validation(self,validate_data):

    #     course = validate_data.get("course")

    #     if self.course not in validate_data:

    #         raise serializers.ValidationError('Course not exist')

    #     return validate_data 