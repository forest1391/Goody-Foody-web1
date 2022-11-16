import requests
from django.shortcuts import render, redirect
from core.settings import API_URL as root
# from utils.decorators import user_login_required
from utils.decorators import user_login_required

import datetime
from django.utils.datastructures import MultiValueDictKeyError

@user_login_required
def restaurant_detail(request, pk):
    r = requests.get(f'{root}/restaurant/detail/{pk}/', cookies={'sessionid': request.COOKIES['sessionid']})
    result = r.json()
    # if result['success'] is True:
    restaurant = result['data']
    return render(request, 'information.html', {'restaurant': restaurant})
    # else:
    #     message = result['message']
    #     return render(request, 'result.html', {'message': message})

@user_login_required
def restaurant_menu(request, pk):
    r = requests.get(f'{root}/menu/restaurant_menu/{pk}/', cookies={'sessionid': request.COOKIES['sessionid']})
    result = r.json()
    # if result['success'] is True:
    restaurant_menu = result['data']
    return render(request, 'menu.html', {'restaurant_menu':restaurant_menu})




@user_login_required
def add_menu(request):
    if request.method =='GET':
        return render(request, 'menuadd.html')

    restaurant_id=request.POST['restaurant_id']
    name = request.POST['name']
    price = request.POST['price']
    kcal = request.POST['kcal']
    carbohydrate = request.POST['carbohydrate']
    protein = request.POST['protein']
    # fat = request.POST['fat']
    try:
        fat = request.POST['fat']
    except MultiValueDictKeyError:
        fat = False
    sodium = request.POST['sodium']
    subname = request.POST['subname']

    data = {

        'restaurant_id': restaurant_id,
        'name':name,
        'price':price,
        'kcal':kcal,
        'carbohydrate':carbohydrate,
        'protein':protein,
        'fat':fat,
        'sodium':sodium,
        'subname':subname


    }
    r = requests.post(
        f'{root}/menu/add/',
        data=data
        )

    return render(request, 'menu.html', {'restaurant_id':restaurant_id})


@user_login_required
def add_information(request):
    if request.method =='GET':
        return render(request, 'Storeinformation.html')

    name = request.POST['name']
    address = request.POST['address']
    phone = request.POST['phone']
    business_hours= request.POST['business_hours']
    resume = request.POST['resume']
    license_id = request.POST['license_id']
    lat = request.POST['lat']
    lon = request.POST['lon']

    data = {

        'account': request.COOKIES['user_id'],
        'name':name,
        'address':address,
        'phone':phone,
        'business_hours':business_hours,
        'resume':resume,
        'license_id':license_id,
        'lat':lat,
        'lon':lon


    }
    r = requests.post(
        f'{root}/restaurant/add/',
        data=data
        )

    return render(request, 'information.html')