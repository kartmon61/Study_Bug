from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.
class University(models.Model):
    name = models.CharField(max_length=100, unique=True)
    department = models.CharField(max_length=100, unique=True)
    grade = models.IntegerField()



class Student(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User,on_delete=True,null=True,default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #university = models.ForeignKey(University,on_delete=models.CASCADE)
    rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    body = models.TextField()
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, related_name='comments')
    author = models.ForeignKey(User,on_delete=True,null=True,default=1)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
    