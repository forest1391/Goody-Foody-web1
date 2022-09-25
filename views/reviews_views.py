import requests
from django.shortcuts import render, redirect
from core.settings import API_URL as root
# from utils.decorators import user_login_required
from utils.decorators import user_login_required




# @user_login_required
def index(request):
    return render(request, 'index.html')

@user_login_required
def analyze(request):
    return render(request, 'analyze.html')

# @user_login_required
# def coming(request):
#     return render(request, 'coming.html')

# @user_login_required
# def contact(request):
#     return render(request, 'contact.html')

# @user_login_required
# def single(request):
#     return render(request, 'single.html')

# @user_login_required
def login(request):
    return render(request, 'login.html')

# @user_login_required
# def post(request):
#     return render(request, 'community.html')

@user_login_required
def communitypage(request):
    return render(request, 'communitypage.html')

@user_login_required
def communitypage2(request):
    return render(request, 'communitypage2.html')

@user_login_required
def Userintroduction(request):
    return render(request, 'Userintroduction.html')

@user_login_required
def consult(request):
    return render(request, 'consult.html')


@user_login_required
def menu(request):
    r = requests.get(
        f'{root}/menu_review/all/',
        cookies={'sessionid': request.COOKIES['sessionid']}
    )
    result = r.json()
    menus = result['data']
    return render(request, 'menu.html', {'menus': menus})

@user_login_required
def post(request):
    r1 = requests.get(
        f'{root}/post/post/',
        cookies={'sessionid': request.COOKIES['sessionid']}
    )

    r2 = requests.get(
        f'{root}/tag/all/',
        cookies={'sessionid': request.COOKIES['sessionid']}
    )
    result1 = r1.json()
    result2 = r2.json()
    # print(result)
    posts = result1['data']
    tags = result2['data']
    return render(request, 'community.html', {'posts': posts,'tags':tags})




@user_login_required
def add(request):
    if request.method =='GET':
        return render(request, 'newpost.html')

    post_id = request.POST['post_id']
    title = request.POST['title']
    content = request.POST['content']

    data = {
        'post_id':post_id,
        'title':title,
        'content':content

    }
    r = requests.post(
        f'{root}/post/add/',
        data=data
        )

    return redirect('/community/')


@user_login_required
def information(request):
    return render(request, 'information.html')

@user_login_required
def comment(request):
    return render(request, 'comment.html')

@user_login_required
def consultchatroom(request):
    return render(request, 'consultchatroom.html')

@user_login_required
def menuadd(request):
    return render(request, 'menuadd.html')

@user_login_required
def storeinformation(request):
    return render(request, 'Storeinformation.html')

@user_login_required
def map(request):
    return render(request, 'map.html')

@user_login_required
def member(request):
    return render(request, 'member.html')

@user_login_required
def newpost(request):
    return render(request, 'newpost.html')

@user_login_required
def verify_diet(request):
    return render(request, 'verify_diet.html')

user_login_required
def verify_store(request):
    return render(request, 'verify_store.html')

# @user_login_required
# def add(request):
#     if request.method == 'GET':
#         return render(request, 'newpost.html')
#
#     post_id = request.POST['post_id']
#     title = request.POST['title']
#     content = request.POST['content']
#
#     data = {
#         'post_id': post_id,
#         'title': title,
#         'content': content,
#     }
#     r = requests.post(
#         f'{root}/post/add/',
#         data=data
#     )
#     result = r.json()
#     return render(request, 'community.html')

