
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

# Create your models here.
class User(AbstractUser):
    phone=models.CharField(max_length=15,unique=True)
    ROLE_CHOICES=[
        ("Trainer","trainer"),
        ("Student","student")
    ]
    role=models.CharField(max_length=10,choices=ROLE_CHOICES,default="student")

    def __str__(self):
        return self.user.username

class StudentProfile(models.Model):

   date_of_birth=models.DateField(null=True,blank=True)
   bio_data=models.TextField(null=True,blank=True)
   GENDER=[
       ("male","Male"),
       ("female","Female")
   ]
   gender=models.CharField(max_length=10,choices=GENDER,default="student")
   student=models.OneToOneField(User,on_delete=models.CASCADE,related_name='student')
   passout_year = models.CharField(max_length=4,null=True)
   skill = models.CharField(max_length=200,null=True)
   address=models.CharField(max_length=200)
   profile_picture=models.ImageField(upload_to="profile_picture",null=True)
   linkedin=models.URLField(null=True)
   qualification = models.CharField(max_length=200,null=True)
   github=models.URLField(null=True)

   def __str__(self):
        return self.user.username
   
class TrainerProfile(models.Model):
       
       date_of_birth=models.DateField(null=True,blank=True)
       bio_data=models.TextField()
       GENDER=[
           ("male","Male"),
           ("female","Female")
       ]
       gender=models.CharField(max_length=10,choices=GENDER,default="student")
       trainer=models.OneToOneField(User,on_delete=models.CASCADE,related_name='trainer')
       profile_picture=models.ImageField(upload_to="profile_picture",null=True)
       github=models.URLField(null=True)
       linkedin=models.URLField(null=True)   
       qualification = models.CharField(max_length=200,null=True)  
       department = models.CharField(max_length=200,null=True,blank=True)

       def __str__(self):
        return self.user.username

def create_profile(sender,instance,created,*args,**kwargs):

    if created:

        if instance.role == 'trainer':

            TrainerProfile.objects.create(trainer=instance)

        elif instance.role == 'student':

            StudentProfile.objects.create(student=instance)

post_save.connect(create_profile,sender=User)                