import requests
from django.shortcuts import render, redirect
from core.settings import API_URL as root
# from utils.decorators import user_login_required
from utils.decorators import user_login_required

def add_photo(request):
    submitted = False

# @user_login_required
# def add_eating(request):
#     if request.method == 'GET':
#         return render(request, 'add_eating.html')