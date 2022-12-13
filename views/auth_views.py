import requests
from django.shortcuts import render, redirect

from core.settings import API_URL as root
from utils.decorators import user_login_required



root += '/auth'


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
    # btn_value = request.POST['rank_id']
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
        # ret.set_cookie('btn', btn_value)
        ret.set_cookie('sessionid', result['sessionid'])
        ret.set_cookie('rank', btn_value)
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

    # btn_value = None
    # if 'user1' in request.POST:
    #     btn_value = request.POST['user1']
    # elif 'user2' in request.POST:
    #     btn_value = request.POST['user2']
    # elif 'user3' in request.POST:
    #     btn_value = request.POST['user3']

    account = request.POST['account']
    password = request.POST['password']
    # btn_value = request.POST['rank']

    data = {
        'account': account,
        'password': password,
        # 'btn_value': btn_value
    }

    r = requests.post(
        f'{root}/register/',
        data=data
    )
    # print(r.cookies.get_dict())
    # result = r.json()
    # if result['success'] is True:
    #     ret = redirect('/login/')
    #     ret.set_cookie('sessionid', result['sessionid'])
    #     ret.set_cookie('user_id', account)
    #     return ret
    # else:
    #     return redirect('/register/')

    print(r.cookies.get_dict())
    result = r.json()
    # print(result)
    if result['success'] is True:
        return redirect('/login/')
    else:
        return redirect('/register/')
    #

def user1register(request):
    return render(request, 'user2register.html')

    account = request.POST['account']
    password = request.POST['password']
    name = requests.POST['name']
    # btn_value = request.POST['rank']

    data = {
        'account': account,
        'password': password,
        'name': name,
    }

    r = requests.post(
        f'{root}/register/',
        data=data
    )

    print(r.cookies.get_dict())
    result = r.json()
    # print(result)
    if result['success'] is True:
        return redirect('/login/')
    else:
        return redirect('/user2register.htm/')


def user2register(request):
    return render(request, 'user2register.html')
    account = request.POST['account']
    password = request.POST['password']
    name = requests.POST['name']

    # btn_value = request.POST['rank']

    data = {
        'account': account,
        'password': password,
        'name': name

    }

    r = requests.post(
        f'{root}/register/',
        data=data
    )

    print(r.cookies.get_dict())
    result = r.json()
    # print(result)
    if result['success'] is True:
        return redirect('/login/')
    else:
        return redirect('/user2register.htm/')


def user3register(request):
    return render(request, 'user2register.html')
    account = request.POST['account']
    password = request.POST['password']
    name = requests.POST['name']
    num = requests.POST['num']

    # btn_value = request.POST['rank']

    data = {
        'account': account,
        'password': password,
        'name': name,
        'num': num

    }

    r = requests.post(
        f'{root}/register/',
        data=data
    )

    print(r.cookies.get_dict())
    result = r.json()
    # print(result)
    if result['success'] is True:
        return redirect('/login/')
    else:
        return redirect('/user2register.htm/')


# def forget(request):
#     if request.method == 'GET':
#         return render(request, 'Forget.html')
#
#     if request.method == "POST":
#
#         account = request.POST['account']
#
#         data = {
#             'account': account,
#         }
#         r = requests.post(
#             f'{root}/forget/',
#             data=data,
#         )
#
#         result = r.json()
#
#         if result['success'] is True:
#
#             import random
#             from core.urls import account
#
#             # 产生随机8位密码
#             random_password = ""
#             for x in range(8):
#                 random_num = str(random.randint(0, 9))
#                 random_low_alpha = chr(random.randint(97, 122))
#                 random_upper_alpha = chr(random.randint(65, 90))
#                 random_char = random.choice([random_num, random_low_alpha, random_upper_alpha])
#                 random_password += random_char
#
#             # 重置密码
#             # username[0].set_password(random_password) # 會有錯誤
#
#             # username[0].password = make_password('random_password')
#             # username[0].save()
#
#             data = {
#                 'account': account,
#                 'password': random_password
#             }
#             requests.post(
#                 f'{root}/forget/reset/',
#                 data=data,
#             )
#
#             # 发送重置密码邮件
#             content_plain = "您好,您收到這封郵件,是因為你選擇了忘記密碼,因此我們為您重置了密碼,新的密碼為: %s" % random_password
#             account = account(
#                 smtp_server='smtp.gmail.com',
#                 from_addr='axxxx@gmail.com', #發送郵件的帳號
#                 password='xxxxx',　#郵件帳號的密碼
#                 to_addr = account,
#                 type = 'plain',
#                 title = '變更密碼',
#                 content = content_plain
#             )
#             flag = account.send_msg()
#             # 邮件发送成功标记
#             if flag == 1:
#                 # return render(request, 'forget_pass.html', {'success': "重置密码已发邮件"})
#                 ret = redirect('/login/')
#                 # messages.success(request, '密碼已重置，請去郵箱查收')
#                 return ret
#
#             # 邮件发送失败反馈
#             else:
#                 ret = redirect('/forget/')
#                 # messages.success(request, '郵件發送失敗，請確認此郵箱是否存在')
#                 return ret
#                 # return render(request, 'forget_pass.html', {'send_email_failed': flag})
#         else:
#             # messages.error(request, '查無此帳號')
#             return redirect('/forget/')
#             return ret