from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from user import models


# join


def joinform(request):
    return render(request, 'user/joinform.html')


def joinsuccess(request):
    return render(request, 'user/joinsuccess.html')


def join(request):
    name = request.POST['name']
    email = request.POST['email']
    password = request.POST['password']
    gender = request.POST['gender']

    models.insert(name, email, password, gender)

    return HttpResponseRedirect('/user/joinsuccess')


# login/logout


def loginform(request):
    return render(request, 'user/loginform.html')


def login(request):
    email = request.POST['email']
    password = request.POST['password']

    result = models.findby_email_and_password(email, password)

    # user info가 틀리면 다시 로그인창으로
    # get방식으로 result = fail을 전달하고,
    # 이런 경우에만 로그인이 실패했습니다 문구뜨게하기 (loginform.html 참고)
    if result is None:
        return HttpResponseRedirect('/user/loginform?result=fail')

    # login 처리
    request.session['authuser'] = result

    return HttpResponseRedirect('/')


def logout(request):
    # logout 처리 : session 쿠키를 삭제
    del request.session['authuser']
    return HttpResponseRedirect('/')


def reqlogin(request):
    return render(request, 'user/reqlogin.html')


# update


def updateform(request):

    #  Access Control (접근 제어) : 로그인 session이 없는 경우 대비
    # 방법1
    # if 'authuser' not in request.session:
    #     return HttpResponseRedirect('/user/loginform')

    # 방법2 (추천)
    authuser = request.session.get('authuser')
    if authuser is None:
        return HttpResponseRedirect('/')

    authuser = request.session['authuser']
    result = models.findbyno(authuser['no'])
    request.session['temp'] = result
    print(request.session['temp'])

    return render(request, 'user/updateform.html')


def update(request):
    # 임시 session 종료
    del request.session['temp']

    # POST방식으로 입력값 받아와 회원정보 update
    name = request.POST['name']
    gender = request.POST['gender']
    no = request.GET['no']
    password = request.POST['password']

    models.update(name, password, gender, no)

    # 수정된 회원 정보로 auhuser session name변경 (no=pk니까 그냥 두기)
    request.session['authuser']['name'] = name

    return HttpResponseRedirect('/user/updatesuccess')


def updatesuccess(request):
    return render(request, 'user/updatesuccess.html')







