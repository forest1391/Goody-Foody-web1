import requests
from django.shortcuts import render, redirect
from core.settings import API_URL as root
# from utils.decorators import user_login_required
from utils.decorators import user_login_required
import datetime




# @user_login_required
def index(request):
    r1 = requests.get(
        f'{root}/post/all/',
        cookies={'sessionid': request.COOKIES['sessionid']}
    )

    r2 = requests.get(
        f'{root}/restaurant/all/',
        cookies={'sessionid': request.COOKIES['sessionid']}
    )

    r3= requests.get(
        f'{root}/tag/all/',
        cookies={'sessionid': request.COOKIES['sessionid']}
    )
    result1 = r1.json()
    result2 = r2.json()
    result3 = r3.json()
    restaurants = result2['data']
    posts = result1['data']
    tags = result3['data']
    return render(request, 'index.html', {'restaurants': restaurants,'posts':posts,'tags':tags})

@user_login_required
def analyze(request):
    r = requests.get(
        f'{root}/analyze/all/',
        cookies={'sessionid': request.COOKIES['sessionid']}
    )
    result = r.json()
    eatings = result['data']
    return render(request, 'analyze.html', {'eatings': eatings})

@user_login_required
def search(request):
    user_id = request.GET.get('user_id')
    r = requests.get(
        f'{root}/eating/detail/',
        params={'user_id': user_id},
        cookies={'sessionid': request.COOKIES['sessionid']}
    )
    data = r.json()
    books = data['data']
    return render(request, 'critic_reviews.html', {'books': books})

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
def report_done(request):
    return render(request, 'report_done.html')

@user_login_required
def communitypage2(request):
    return render(request, 'communitypage2.html')

@user_login_required
def Userintroduction(request):
    return render(request, 'Userintroduction.html')



@user_login_required
def add_eating(request):
    if request.method == 'GET':
        return render(request, 'add_eating.html')

    menu_id = request.POST['menu_id']
    eat_type_id = request.POST['eat_type_id']
    kcal = request.POST['kcal']
    carbohydrate = request.POST['carbohydrate']
    protein = request.POST['protein']
    fat = request.POST['fat']
    sodium = request.POST['sodium']

    data = {

        'account': request.COOKIES['user_id'],
        'menu_id': menu_id,
        'eat_type_id': eat_type_id,
        'date': datetime.date.today(),
        'kcal': kcal,
        'carbohydrate':carbohydrate,
        'protein':protein,
        'fat':fat,
        'sodium':sodium

    }
    r = requests.post(
        f'{root}/analyze/add/',
        data=data
    )

    return redirect('/map/')

@user_login_required
def add_report(request):
    if request.method == 'GET':
        return render(request, 'add_report.html')

    title = request.POST['title']
    content = request.POST['content']
    date = request.POST['date']

    data = {

        'account': request.COOKIES['user_id'],
        # 'date': datetime.date.today(),
        'date': date,
        'title': title,
        'content': content,

    }
    r = requests.post(
        f'{root}/report/add/',
        data=data
    )

    return redirect('/report_done/')


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
        f'{root}/post/all/',
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


    title = request.POST['title']
    content = request.POST['content']

    data = {

        'account': request.COOKIES['user_id'],
        'title':title,
        'post_time':datetime.date.today(),
        'content':content,
        # 'pic':str(base64.b64encode(photo.read()))[2;-1]


    }
    r = requests.post(
        f'{root}/post/add/',
        data=data
        )

    return redirect('/community/')

@user_login_required
def latlng(request):
    if request.method =='GET':
        return render(request, 'add_post.html')

    lat = request.POST['lat']
    lng = request.POST['lng']

    data = {

        'lng': lng,
        'lat':lat,

    }
    r = requests.post(
        f'{root}/post/add/',
        data=data
        )

    return redirect('/map/')

@user_login_required
def add_tag(request):
    if request.method =='GET':
        return render(request, 'add_tag.html')

    # tag_id = request.POST['tag_id']
    tag_name = request.POST['tag_name']
    tag_type_id = request.POST['tag_type_id']

    data = {
        # 'tag_id':tag_id,
        'tag_name':tag_name,
        'tag_type_id':tag_type_id

    }
    r = requests.post(
        f'{root}/tag/add/',
        data=data
        )

    return redirect('/community/')



@user_login_required
def add_chat(request):
    # if request.method =='GET':
    #     return render(request, 'add_eating.html')
    chat_id = request.POST['chat_id']
    account = request.POST['account']
    b_account = request.POST['b_account']
    time = request.POST['time']
    content = request.POST['content']

    data = {
        'chat_id': chat_id,
        'account': account,
        'b_account': b_account,
        'time':time,
        'content': content
    }
    r = requests.post(
        f'{root}/chat/add/',
        data=data
        )

    return redirect('/consultchatroom/')



@user_login_required
def information(request):
    return render(request, 'information.html')

@user_login_required
def comment(request):
    return render(request, 'comment31.html')

@user_login_required
def consultchatroom(request):
    return render(request, 'consultchatroom.html')

@user_login_required
def menuadd(request):
    return render(request, 'menuadd.html')

@user_login_required
def chat(request):
    r = requests.get(
        f'{root}/chat/all/',
        cookies={'sessionid': request.COOKIES['sessionid']}
    )
    result = r.json()
    chats = result['data']
    return render(request, 'consultchatroom.html', {'chats': chats})

@user_login_required
def storeinformation(request):
    return render(request, 'Storeinformation.html')

@user_login_required
def map(request):
    r1 = requests.get(
        f'{root}/restaurant/all/',
        cookies={'sessionid': request.COOKIES['sessionid']}
    )
    r2 = requests.get(
        f'{root}/tag/all/',
        cookies={'sessionid': request.COOKIES['sessionid']}
    )

    result1 = r1.json()
    result2 = r2.json()

    restaurants = result1['data']
    tags = result2['data']
    return render(request, 'map.html',{'restaurants': restaurants,'tags':tags})
    # return render(request, 'member.html')
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

@user_login_required
def get_a_post(request):
    post_id = request.GET.get('post_id')
    r = requests.get(
        f'{root}/post/detail/',
        params={'post_id': post_id},
        cookies={'sessionid': request.COOKIES['sessionid']}
    )
    data = r.json()
    books = data['data']
    return render(request, 'community.html', {'posts': posts})

