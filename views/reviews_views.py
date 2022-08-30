import requests
from django.shortcuts import render, redirect
from core.settings import API_URL as root
from utils.decorators import user_login_required

root += 'menu_review'

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

@user_login_required
def community(request):
    return render(request, 'community.html')

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
        f'{root}/all/',
        cookies={'sessionid': request.COOKIES['sessionid']}
    )
    result = r.json()
    menus = result['data']
    return render(request, 'menu.html', {'menus': menus})

@user_login_required
def information(request):
    return render(request, 'information.html')

# @user_login_required
# def comment(request):
#     return render(request, 'comment.html')

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


# @user_login_required
# def comment(request):
#     r = requests.get(
#         f'{root}/all/',
#         cookies={'sessionid': request.COOKIES['sessionid']}
#     )
#     if r.status_code == 401:
#         return redirect('/logout/')

#     result = r.json()
#     restaurant_msgs = result['data']
#     return render(request, 'comment.html', {'restaurant_msgs': restaurant_msgs})

# <test>
# def regist40(request):
#     return render(request, 'regist40.html')

# def comment_add(request):
#     return render(request, 'comment.html')

# def deletemsg40(request):
#     if request.method == 'GET':
#         return render(request, 'deletemsg40.html')

#     restaurant_msg_id = request.POST['restaurant_msg_id']
#     data = {
#         'account': request.COOKIES['account']
#     }

#     r = requests.post(
#         f'{root}/deletemsg40/{restaurant_msg_id}/',
#         data=data,
#         cookies={'sessionid': request.COOKIES['sessionid']}
#     )
#     result = r.json()
#     return render(request, 'deletemsg40.html', {'message': result['message']})
#   <test>

# <test2>
# @user_login_required
# def comment(request):
#     r = requests.get(
#         f'{root}/all/',
#         cookies={'sessionid': request.COOKIES['sessionid']}
#     )
#     if r.status_code == 401:
#         return redirect('/logout/')

#     result = r.json()
#     restaurant_msgs = result['data']
#     return render(request, 'comment.html', {'restaurant_msgs': restaurant_msgs})



# def comment_add(request):
#     if request.method == 'GET':
#         return render(request, 'comment.html')
#     restaurant_msg_id=request.POST['restaurant_msg_id']
#     restaurant_id = request.POST['restaurant_id']
#     content	 = request.POST['content']
#     time = request.POST['time']
#     data = {
#         'restaurant_msg_id': restaurant_msg_id,
#         'restaurant_id': restaurant_id,
#         'account': test_account,
#         'content': content,
#         'time': time,
#     }
#     r = requests.post(
#         f'{root}/add/',
#         data=data,
#     )
#     result = r.json()
#     return render(request, 'comment.html', {'message': result['message']})

# @user_login_required
# def detail(request, pk):
#     r = requests.get(
#         f'{root}/get/{pk}/',
#         cookies={'sessionid': request.COOKIES['sessionid']}
#     )
#     result = r.json()
#     if result['success'] is True:
#         book = result['data']
#         return render(request, 'detail.html', {'book': book})
#     else:
#         message = result['message']
#         return render(request, 'result.html', {'message': message})


# @user_login_required
# def search(request):
#     user_id = request.GET.get('user_id')
#     r = requests.get(
#         f'{root}/get_critic_reviews/',
#         params={'user_id': user_id},
#         cookies={'sessionid': request.COOKIES['sessionid']}
#     )
#     data = r.json()
#     books = data['data']
#     return render(request, 'critic_reviews.html', {'books': books})


# @user_login_required
# def edit(request):
#     if request.method == 'GET':
#         return render(request, 'edit_form.html')

#     book_no = request.POST['book_no']
#     title = request.POST['title']
#     name = request.POST['name']
#     comment = request.POST['comment']

#     data = {
#         'user_id': request.COOKIES['user_id'],
#         'title': title,
#         'name': name,
#         'comment': comment
#     }

#     r = requests.post(
#         f'{root}/edit/{book_no}/',
#         data=data,
#         cookies={'sessionid': request.COOKIES['sessionid']}
#     )
#     result = r.json()
#     return render(request, 'result.html', {'message': result['message']})

# @user_login_required
# def delete(request):
#     if request.method == 'GET':
#         return render(request, 'deletemsg40.html')

#     restaurant_msg_id  = request.POST['restaurant_msg_id ']
#     data = {
#         'account': request.COOKIES['account']
#     }

#     r = requests.post(
#         f'{root}/deletemsg40/{restaurant_msg_id }/',
#         data=data,
#         cookies={'sessionid': request.COOKIES['sessionid']}
#     )
#     result = r.json()
#     return render(request, 'result.html', {'message': result['message']})

# <test2>

