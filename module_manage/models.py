from django.db import models

from course_manage.models import Course

from accounts.models import User

class Module(models.Model):

    name = models.CharField(max_length=200)

    description = models.TextField(null=True,blank=True)

    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name="modules")

    trainer = models.ForeignKey(User,on_delete=models.CASCADE)

    topics = models.TextField()

    module_number = models.PositiveIntegerField(null=True,blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):

        last_obj = Module.objects.filter(course=self.course).last()

        if last_obj  and last_obj.module_number is not None:

          self.module_number = last_obj.module_number+1

        else:
            self.module_number = 1

            return super().save(*args,**kwargs)  

    def total_modules(self):
        return Module.objects.filter(course=self).count()           