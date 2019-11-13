from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class University(models.Model):
    name = models.CharField(max_length=100, unique=True)
    department = models.CharField(max_length=100, unique=True)
    grade = models.IntegerField()

    def __str__(self):
        return '%s - %s - %s' % (self.name,self.department,self.grade)


class Student(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    university = models.ForeignKey(University,on_delete=models.CASCADE)
    rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    body = models.TextField()