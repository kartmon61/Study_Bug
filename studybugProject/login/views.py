from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'login.html')


# 로딩 화면     
def loading(request):
    return render(request,'loading.html')
