from django.db import models
from accounts.models import User
from module_manage.models import Module
# Create your models here.
class Lessons(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField(null=True,blank=True)

    module = models.ForeignKey(Module,on_delete=models.CASCADE,related_name="lessons")

    trainer = models.ForeignKey(User,on_delete=models.CASCADE)

    video_url = models.URLField(null=True,blank=True)

    lesson_no=  models.PositiveIntegerField(null=True,blank=True)

    duration = models.CharField(max_length=50,null=True,blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):

        return self.title

    def save(self, *args, **kwargs):
         last_obj = Lessons.objects.filter(module=self.module).last()

         if last_obj:
             self.lesson_no=last_obj.lesson_no+1
         else:
             self.lesson_no=1
         return super().save(*args,**kwargs) 
