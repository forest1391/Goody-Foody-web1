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
    r = requests.get(
        f'{root}/analyze/all/',
        cookies={'sessionid': request.COOKIES['sessionid']}
    )
    result = r.json()
    eatings = result['data']
    return render(request, 'analyze.html', {'eatings': eatings})

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
def add_eating(request):
    return render(request, 'add_eating.html')


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
        return render(request, 'add_post.html')

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
def add_tag(request):
    if request.method =='GET':
        return render(request, 'add_tag.html')

    tag_id = request.POST['tag_id']
    tag_name = request.POST['tag_name']
    tag_type_id = request.POST['tag_type_id']

    data = {
        'tag_id':tag_id,
        'tag_name':tag_name,
        'tag_type_id':tag_type_id

    }
    r = requests.post(
        f'{root}/tag/add/',
        data=data
        )

    return redirect('/community/')

@user_login_required
def add_eating(request):
    if request.method =='GET':
        return render(request, 'add_eating.html')

    eat_id = request.POST['eat_id']
    account = request.POST['account']
    menu_id = request.POST['menu_id']
    eat_type_id = request.POST['eat_type_id']
    date = request.POST['date']
    kcal = request.POST['kcal']
    carbohydrate = request.POST['carbohydrate']
    fat = request.POST['fat']
    protein = request.POST['protein']

    data = {
        'eat_id': eat_id,
        'account': account,
        'menu_id': menu_id,
        'eat_type_id':eat_type_id,
        'date': date,
        'kcal':kcal,
        'carbohydrate':carbohydrate,
        'fat':fat,
        'protein':protein

    }
    r = requests.post(
        f'{root}/eating/add/',
        data=data
        )

    return redirect('/analyze/')



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
    r = requests.get(
        f'{root}/restaurant/all/',
        cookies={'sessionid': request.COOKIES['sessionid']}
    )
    result = r.json()
    restaurants = result['data']
    return render(request, 'map.html', {'restaurants': restaurants})

@user_login_required
def member(request):
    return render(request, 'member.html')

@user_login_required
def newpost(request):
    return render(request, 'add_post.html')

@user_login_required
def verify_diet(request):
    return render(request, 'verify_diet.html')

@user_login_required
def verify_store(request):
    return render(request, 'verify_store.html')

# @user_login_required
# def add(request):
#     if request.method == 'GET':
#         return render(request, 'add_post.html')
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

