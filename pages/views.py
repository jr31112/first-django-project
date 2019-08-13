import random

from django.shortcuts import render

# Create your views here.

# 2. 요청을 처리할 함수 정의
def index(request):
    # 2. >> 로직 작성 <<
    # 3. 해당하는 템플릿 반환
    return render(request, 'index.html')

def hello(request, name):
    context = {'name':name}
    return render(request, 'hello.html',context)

def lotto(request):
    print(request)
    print(type(request))
    print(request.META)
    # 로직
    numbers = sorted(random.sample(range(1, 46), 6))
    # 변수를 딕셔너리에 담아서(보통 context라고 부름) 보낸다.
    context = {'numbers' : numbers}
    # render 할때 3번째 인자로 넘겨준다.
    # render 함수의 필수 인자 : request, template 파일
    # 변수를 넘겨 주고 싶으면 3번째 인자로 dictionary를 넘겨준다.
    # Django에서 활용하는 템플릿 언어는 Django Template Laguage이다.
    return render(request, 'lotto.html', context)

import datetime
def dinner(request):
    menus = ['롯데리아', '편도', '맘스터치', '응급실떡볶이', '노은각', '피자', '치킨']
    pick = random.choice(menus)
    context = {'pick' : pick, 'menus' : menus, 'users' : [], 'sentence' : 'Life is short, You need Python + django', 'datetime_now' : datetime.datetime.now(), 'google_link' : 'http://www.google.com'}
    return render(request, 'dinner.html', context)

def cube(request, number):
    context = {'number': number, 'cubenumber':number**3, 'numbers':[1, 2, 3], 'student':{1:'지수',2:'태수'}}
    return render(request, 'cube.html', context)

def about(request, name, age):
    context = {'name':name, 'age':age}
    return render(request, 'about.html', context)

def isitgwangbok(request):
    now = datetime.datetime.now()
    if now.month == 8 and now.day == 15:
        context = {'output':'예'}
    else:
        context = {'output':'아니오'}
    return render(request, 'isitgwangbok.html', context)
    
def ping(request):
    return render(request, 'ping.html')

def pong(request):
    # 사용자가 넘겨주는 값 받아오기
    print(request.GET)
    # QueryDict 일종의 dict, {'data' : '안녕하세요'}
    data = request.GET.get('data')
    context = {
        'data' : data
    }
    return render(request, 'pong.html', context)

def signup(request):
    return render(request, 'signup.html')

def signup_result(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    password_confirmation = request.POST.get('password_confirmation')
    is_signup = True if password == password_confirmation else False
    context = {'is_signup' : is_signup, 'username':username}
    return render(request, 'signup_result.html', context)