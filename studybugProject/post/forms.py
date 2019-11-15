from django import forms
from .models import Student, Comment, License

# 생략
# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         field = ['license_on','rate','body']

#         licenses = (
#             ('a',"산업기사자격증"),
#             ('b',"물류기사자격증"),
#         )

#         license_on = models.CharField(
#             max_length=1,
#             choices = LEVEL,
#             blank = True,
#             default='a',
#             help_text='자격증 종류',
#         )

#         widgets = {
            
#             'rate':CounterTextInput,
#             'body':CounterTextInput,
#         }

# class CommentForm(forms.ModelForm):

#     class Meta:
#         model = Comment
#         fields = ('author', 'text',)

class BlogPost(forms.ModelForm):
    class Meta:
        model =  Student
        fields = ['license_on','rate','body']
        
