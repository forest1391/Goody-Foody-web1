"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path

from views import analyze_views,auth_views,chat_views,comment_views,post_views,restaurant_views,reviews_views


urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', views.index),
    path('', lambda request: redirect('/login/')),  # 直接導向views畫面  lambda
    path('index/', reviews_views.index),
    path('analyze/', analyze_views.analyze),
    path('menu/<int:pk>', restaurant_views.restaurant_menu),
    # path('coming/', reviews_views.coming),
    # path('contact/', reviews_views.contact),
    # path('single/', reviews_views.single),
    path('community/', reviews_views.post),
    path('add_eating/', reviews_views.add_eating),
    # path('communitypage/', reviews_views.communitypage),
    path('communitypage2/', reviews_views.communitypage2),
    path('Userintroduction/', reviews_views.Userintroduction),
    path('consult/', reviews_views.consult),
    path('menu/', reviews_views.menu),
    # path('information/', reviews_views.information),
    path('consultchatroom/', chat_views.chat),
    path('menuadd/', reviews_views.menuadd),
    path('Storeinformation/', reviews_views.storeinformation),
    path('map/', reviews_views.map),
    path('member/', reviews_views.member),
    path('communitypage/<int:pk>/', post_views.post_detail),
    path('information/<int:pk>/', restaurant_views.restaurant_detail),

    path('report/add/', reviews_views.add_report),
    path('information/add/', restaurant_views.add_information),
    path('report_done/', reviews_views.report_done),

    path('verify_diet/', reviews_views.verify_diet),
    path('verify_store/', reviews_views.verify_store),
    path('post/add/', reviews_views.add),
    path('tag/add/', reviews_views.add_tag),
    path('eating/add/', reviews_views.add_eating),
    path('login/', auth_views.login),
    path('logout/', auth_views.logout),
    path('register/', auth_views.register),
    # path('forget/', auth_views.forget),
    path('user2register/', auth_views.user2register),



    # <test>
    # path('comment/<int:pk>', comment_views.comment),
    path('comment/', comment_views.comment),
    # path('comment/add/',comment_views.comment_add),
    # path('regist40/', comment_views.regist40),
    path('deletemsg40/<int:pk>/', comment_views.deletemsg40),

    # <test>
]


