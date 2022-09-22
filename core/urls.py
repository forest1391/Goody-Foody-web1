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

from views import auth_views,reviews_views


urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', views.index),
    path('', lambda request: redirect('/index/')),#直接導向views畫面  lambda
    path('index/', reviews_views.index),
    path('analyze/', reviews_views.analyze),
    # path('coming/', reviews_views.coming),
    # path('contact/', reviews_views.contact),
    # path('single/', reviews_views.single),
    path('community/', reviews_views.post),
    path('add_eating/', reviews_views.add_eating),
    path('communitypage/', reviews_views.communitypage),
    path('communitypage2/', reviews_views.communitypage2),
    path('Userintroduction/', reviews_views.Userintroduction),
    path('consult/', reviews_views.consult),
    path('menu/', reviews_views.menu),
    path('information/', reviews_views.information),
    path('comment/', reviews_views.comment),
    path('consultchatroom/', reviews_views.consultchatroom),
    path('menuadd/', reviews_views.menuadd),
    path('Storeinformation/', reviews_views.storeinformation),
    path('map/', reviews_views.map),
    path('member/', reviews_views.member),
    path('verify_diet/', reviews_views.verify_diet),
    path('verify_store/', reviews_views.verify_store),
    path('post/add/', reviews_views.add),
    path('tag/add/', reviews_views.add_tag),
    path('eating/add/', reviews_views.add_eating),
    path('login/', auth_views.login),
    path('logout/', auth_views.logout),
]
