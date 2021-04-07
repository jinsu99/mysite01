from django.shortcuts import render


def index(request):
    return render(request, 'board/index.html')


def view(request):
    return render(request, 'board/view.html')


def updateform(request):
    return render(request, 'board/updateform.html')


def writeform(request):
    return render(request, 'board/writeform.html')