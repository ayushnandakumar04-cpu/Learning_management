
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    phone=models.CharField(max_length=200)
    ROLE_CHOICES=[
        ("Trainer","trainer"),
        ("Student","student")
    ]
    role=models.CharField(max_length=10,choices=ROLE_CHOICES,default="student")

    def __str__(self):
        return self.user.username

class StudentProfile(models.Model):

   date_of_birth=models.DateField()
   bio_data=models.TextField()
   GENDER=[
       ("male","Male"),
       ("female","Female")
   ]
   gender=models.CharField(max_length=10,choices=GENDER,default="student")
   student=models.OneToOneField(User,on_delete=models.CASCADE)
   address=models.CharField(max_length=200)
   profile_picture=models.ImageField(upload_to="profile_picture",null=True)
   linkedin=models.URLField(null=True)
   github=models.URLField(null=True)
   def __str__(self):
        return self.user.username
   
class TrainerProfile(models.Model):
       
       date_of_birth=models.DateField()
       bio_data=models.TextField()
       GENDER=[
           ("male","Male"),
           ("female","Female")
       ]
       gender=models.CharField(max_length=10,choices=GENDER,default="student")
       trainer=models.OneToOneField(User,on_delete=models.CASCADE)
       profile_picture=models.ImageField(upload_to="profile_picture",null=True)
       github=models.URLField(null=True)
       linkedin=models.URLField(null=True)

       def __str__(self):
        return self.user.username