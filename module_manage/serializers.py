from rest_framework import serializers
from module_manage.models import Module
class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Module
        fields="__all__"
        read_only_fields=["id","created_at","updated_at","course","trainer","module_number"]
    # def course_validation(self,validate_data):

    #     course = validate_data.get("course")

    #     if self.course not in validate_data:

    #         raise serializers.ValidationError('Course not exist')

    #     return validate_data 