from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'login.html')


# 로딩 화면     
def loading(request):
    return render(request,'loading.html')

# 관심사 고르기   
def signup2(request):
    return render(request,'signup2.html')

