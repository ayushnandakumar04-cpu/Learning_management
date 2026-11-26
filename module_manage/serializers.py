from rest_framework import serializers
from module_manage.models import Module
class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Module
        fields="__all__"
        read_only_fields=["id","created_at","updated_at","course","trainer","module_number"]
