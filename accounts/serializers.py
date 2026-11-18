from rest_framework import serializers
from accounts.models import User,StudentProfile,TrainerProfile
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","email","password","phone","role"]
        extra_kwargs = {
            'password': {'write_only': True},
            'role': {'read_only': True}
        }

class StudentProfileSerailizer(serializers.ModelSerializer):

    class Meta:

        model = StudentProfile 

        fields = "__all__"

        read_only_fileds = ["id","student"]      


class TrainerProfileSerializer(serializers.ModelSerializer):

    class Meta:

        model = TrainerProfile

        fields = "__all__"

        read_only_fields = ["id","trainer"]

