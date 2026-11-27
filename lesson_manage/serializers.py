from rest_framework import serializers
from lesson_manage.models import Lessons

class LessonSerializer(serializers.ModelSerializer):
  
     class Meta:
        model=Lessons
        fields="__all__"
        read_only_fields=["id","created_at","updated_at","trainer","module","lesson_no"]

