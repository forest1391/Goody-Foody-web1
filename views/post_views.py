import requests
from django.shortcuts import render, redirect
from core.settings import API_URL as root
# from utils.decorators import user_login_required
from utils.decorators import user_login_required
import datetime

@user_login_required
def post_detail(request, pk):
    r = requests.get(f'{root}/post/detail/{pk}/', cookies={'sessionid': request.COOKIES['sessionid']})
    result = r.json()
    # if result['success'] is True:
    post = result['data']
    return render(request, 'communitypage.html', {'post': post})
    # else:
    #     message = result['message']
    #     return render(request, 'result.html', {'message': message})

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

