from django.contrib import admin
from .models import Student,Comment,License

# Register your models here.
#admin.site.register(University)
admin.site.register(Student)
admin.site.register(Comment)
admin.site.register(License)