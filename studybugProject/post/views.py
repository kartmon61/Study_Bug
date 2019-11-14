from django.shortcuts import render
from django.utils import timezone

from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Student, University, Comment
from django.contrib.auth.models import User

# Create your views here.
class PostView(ListView):   #html 템플릿 : 블로그 리스트를 담은 html : (소문자모델)_list.html
    template_name = 'post/list.html'
    context_object_name = 'comm_list'
    model = Student

class PostCreate(CreateView): #html : form (입력공간)을 갖고 있는 html : (소문자모델)_form.html
    template_name = 'post/create.html'
    model = Student
    fields = ['title','body','rate']
    success_url = reverse_lazy('list')

class PostDetail(DetailView): #html : 상세 페이지를 담은 html : (소문자모델)_detail.html
    template_name = 'post/detail.html'
    context_object_name = 'comm_post'
    model = Student

class PostUpdate(UpdateView): #html : form (입력공간)을 갖고 있는 html : (소문자모델)_form.html
    template_name = 'post/create.html'
    model = Student
    fields = ['title','body','rate']
    success_url = reverse_lazy('list')

class PostDelete(DeleteView): #html : 삭제 확인 html (소문자모델)_confirm_delete.html
    template_name = 'post/delete.html'
    model = Student
    success_url = reverse_lazy('list')

def commentcreate(request,post_id):
    if(request.method == 'POST'):
        one_post = get_object_or_404(Student,id=post_id)
        one_post.comment_set.create(text=request.POST['comment_content'],author=request.POST['comm_nm'])
    return redirect('/main/detail/'+str(post_id))

def commentdelete(request,post_id,comment_id):
        one_comment = get_object_or_404(Comment,id=comment_id,posting=post_id)
        if one_comment.author == User.objects.get(username = request.user.get_username()):
                one_comment = get_object_or_404(Comment,id=comment_id,posting=post_id)
                one_comment.delete()
                return redirect('/main/detail/'+str(post_id))
        else:
                return redirectForm(request, '댓글을 삭제할 수 없습니다.' )


# class CommentUpdate(UpdateView):
#     model = Comment
#     fields = ['text']
#     context_object_name = 'comment_update'
#     template_name = 'post/comment_update.html'

#     def dispatch(self, request, *args, **kwargs):
#         object = self.get_object()
#         if object.author != request.user:
#             messages.warning(request, '수정할 권한이 없습니다.')
#             return HttpResponseRedirect('/')
#             # 삭제 페이지에서 권한이 없다! 라고 띄우거나
#             # detail페이지로 들어가서 삭제에 실패했습니다. 라고 띄우거나
#         else:
#             return super(CommentUpdate, self).dispatch(request, *args, **kwargs)

# class CommentDelete(DeleteView):
#     model = Comment
#     template_name = 'post/comment_delete.html' 
#     success_url = '/'

#     def dispatch(self, request, *args, **kwargs):
#         object = self.get_object()
#         if object.author != request.user:
#             messages.warning(request, '삭제할 권한이 없습니다.')
#             return HttpResponseRedirect('/')
#         else:
#             return super(CommentDelete, self).dispatch(request, *args, **kwargs)