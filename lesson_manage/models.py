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

    duration = models.CharField(max_length=50,null=True,blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):

        return self.title

    def total_lessons(self):
        return Lessons.objects.filter(module=self).count()   