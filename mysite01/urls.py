"""mysite01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path
import main.views as mainviews
import guestbook.views as guestbookview
import user.views as userview
import board.views as boardview

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', mainviews.index),

    # guestbook
    path('guestbook/', guestbookview.index),
    path('guestbook/add', guestbookview.add),
    path('guestbook/delete', guestbookview.delete),
    path('guestbook/deleteform', guestbookview.deleteform),

    # user
    path('user/joinform', userview.joinform),
    path('user/joinsuccess', userview.joinsuccess),
    path('user/join', userview.join),
    path('user/loginform', userview.loginform),
    path('user/login', userview.login),
    path('user/logout', userview.logout),
    path('user/updateform', userview.updateform),
    path('user/update', userview.update),
    path('user/updatesuccess', userview.updatesuccess),
    path('user/reqlogin', userview.reqlogin),

    # board
    path('board/', boardview.index),
    path('board/views', boardview.view),
    path('board/updateform', boardview.updateform),
    path('board/update', boardview.update),
    path('board/writeform', boardview.writeform),
    path('board/write', boardview.write),
    path('board/replyform', boardview.replyform),
    path('board/reply', boardview.reply),
    path('board/delete', boardview.delete),
    path('board/deletealert', boardview.deletealert),
    path('board/search', boardview.search),
    path('board/searchlist', boardview.searchlist),

]
