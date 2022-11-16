import requests
from django.shortcuts import render, redirect
from core.settings import API_URL as root
# from utils.decorators import user_login_required
from utils.decorators import user_login_required
import datetime

#
# @user_login_required
# def meal(request):
#     eat_type_id = request.GET.get('eat_type_id')
#     r = requests.get(
#         f'{root}/analyze/meal/',
#         params={'eat_type_id': eat_type_id},
#         cookies={'sessionid': request.COOKIES['sessionid']}
#     )
#     data = r.json()
#     books = data['data']
#     return render(request, 'critic_reviews.html', {'books': books})

@user_login_required
def add_eating(request):
    if request.method =='GET':
        return render(request, 'add_eating.html')


    menu_id = request.POST['menu_id']
    eat_type_id = request.POST['eat_type_id']
    date = request.POST['date']
    kcal = request.POST['kcal']
    carbohydrate = request.POST['carbohydrate']
    fat = request.POST['fat']
    protein = request.POST['protein']
    sodium = request.POST['sodium']

    data = {

        'account': request.COOKIES['user_id'],
        'menu_id': menu_id,
        'eat_type_id':eat_type_id,
        'date': date,
        'kcal':kcal,
        'carbohydrate':carbohydrate,
        'fat':fat,
        'protein':protein,
        'sodium':sodium

    }
    # tkcal += kcal
    # tcar += carbohydrate
    # tpro += protein
    # tfat += fat
    # total = {'tkcal': tkcal, 'tcar':tcar, 'tpro':tpro ,'tfat':tfat}
    r = requests.post(
        f'{root}/analyze/add/',
        data=data
        )

    return redirect('/analyze/')


@user_login_required
def add_menu_item(request, no):
    # search menu_id detail
    r = requests.get(
        f'{root}/analyze/add_menu_item/{no}/',
        cookies={'sessionid': request.COOKIES['sessionid']}
    )
    result = r.json()
    detail=result['data']
    data = {

        'account': request.COOKIES['user_id'],
        'menu_id': no,
        'eat_type_id':detail['eat_type_id'],
        'date': datetime.now(),
        'kcal':detail['kcal'],
        'carbohydrate':detail['carbohydrate'],
        'fat':detail['fat'],
        'protein':detail['protein'],
    }
    
    # result = r.json()
    # true -> detail data




@user_login_required
def analyze(request):
    # total
    r = requests.get(
        f'{root}/analyze/all/',
        cookies={'sessionid': request.COOKIES['sessionid']}
    )

    # breakfast
    r1 = requests.get(
        f'{root}/analyze/meal/1/',
        cookies={'sessionid': request.COOKIES['sessionid']}
    )
    # lunch
    r2 = requests.get(
        f'{root}/analyze/meal/2/',
        cookies={'sessionid': request.COOKIES['sessionid']}
    )
    # dinner
    r3 = requests.get(
        f'{root}/analyze/meal/3/',
        cookies={'sessionid': request.COOKIES['sessionid']}
    )

    result = r.json()
    result1 = r1.json()
    result2 = r2.json()
    result3 = r3.json()

    eatings = result['data']
    breakfast = result1['data']
    lunch = result2['data']
    dinner = result3['data']

    kcal = 0
    carbohydrate = 0
    protein = 0
    fat = 0
    for eating in eatings:
        kcal += eating['kcal']
        carbohydrate += eating['carbohydrate']
        protein += eating['protein']
        fat += eating['fat']

    return render(request, 'analyze.html', {'eatings': eatings, 'breakfast':breakfast, 'lunch':lunch, 'dinner':dinner , 'kcal':kcal, 'carbohydrate':carbohydrate, 'protein':protein, 'fat':fat})