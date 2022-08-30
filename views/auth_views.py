import requests
from django.shortcuts import render, redirect

from core.settings import API_URL as root
from utils.decorators import user_login_required

root += 'auth'

def login(request):
    if 'user_id' in request.COOKIES:
        return redirect('/index/')
    if request.method == 'GET':
        return render(request, 'login.html')

    btn_value = None
    if 'user1' in request.POST:
        btn_value = request.POST['user1']
    elif 'user2' in request.POST:
        btn_value = request.POST['user2']
    elif 'user3' in request.POST:
        btn_value = request.POST['user3']

    # html
    user_id = request.POST['account']
    pwd = request.POST['password']
    # api
    data = {
        'account': user_id,
        'password': pwd,
        'btn_value': btn_value
    }
    r = requests.post(
        f'{root}/login/',
        data=data
    )
    # print(r.cookies.get_dict())
    result = r.json()
    if result['success'] is True:
        ret = redirect('/index/')
        ret.set_cookie('sessionid', result['sessionid'])
        ret.set_cookie('user_id', user_id)
        return ret
    else:
        return redirect('/login/')


@user_login_required
def logout(request):
    r = requests.post(
        f'{root}/logout/',
        cookies={'sessionid': request.COOKIES['sessionid']}
    )
    ret = redirect('/login/')
    ret.delete_cookie('user_id')
    ret.delete_cookie('sessionid')
    return ret


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')

    btn_value = None
    if 'user1' in request.POST:
        btn_value = request.POST['user1']
    elif 'user2' in request.POST:
        btn_value = request.POST['user2']
    elif 'user3' in request.POST:
        btn_value = request.POST['user3']

    account = request.POST['account']
    password = request.POST['password']
    btn_value = request.POST['rank']

    data = {
        'account': account,
        'password': password,
        'btn_value': btn_value
    }

    r = requests.post(
        f'{root}/login/',
        data=data
    )
    # print(r.cookies.get_dict())
    result = r.json()
    if result['success'] is True:
        ret = redirect('/login/')
        ret.set_cookie('sessionid', result['sessionid'])
        ret.set_cookie('user_id', user_id)
        return ret
    else:
        return redirect('/login/')
