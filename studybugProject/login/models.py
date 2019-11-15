from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User_info(models.Model):
    user = models.ForeignKey(User,on_delete=True,null=True,default=1)
    user_interest = models.CharField(max_length=200,null=True)
    #user_img = models.ImageField()

# class Category(models.Model):
#     CATEGORY = (
#         (0,'경영'),
#         (1,'물류'),
#         (2,'화학'),
#         (3,'건축'),
#         (4,'전기'),
#         (5,'컴퓨터'),
#     )
#     codeNum = models.IntegerField(max_length=5,default=0 choices=CATEGORY)