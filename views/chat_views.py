import requests
from django.shortcuts import render, redirect
from core.settings import API_URL as root
# from utils.decorators import user_login_required
from utils.decorators import user_login_required
import datetime


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
def add_chat(request):
    if request.method =='GET':
        return render(request, 'consultchatroom.html')

    b_account = request.POST['b_account']
    content = request.POST['content']
    time = request.POST['time']

    data = {
        'account': request.COOKIES['user_id'],
        'b_account':b_account,
        'content':content,
        'time':time
    }
    r = requests.post(
        f'{root}/chat/add/',
        data=data
        )

    return redirect('/chat/add/')

@user_login_required
def chat_and_add(request):
    if request.method =='GET':
        return render(request, 'consultchatroom.html')

    b_account = request.POST['b_account']
    content = request.POST['content']
    time = request.POST['time']

    data = {
        'account': request.COOKIES['user_id'],
        'b_account':b_account,
        'content':content,
        'time':time
    }

    r = requests.get(
        f'{root}/chat/chat/',
        cookies={'sessionid': request.COOKIES['sessionid']}
    )
    result = r.json()
    chats = result['data']


    return render(request, 'consultchatroom.html', {'chats': chats})

