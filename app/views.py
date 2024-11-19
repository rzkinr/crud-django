from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Users
from django.contrib import messages
from django.db.models.query import Q
from .utilities import ppn11persen
import json


# Create your views here.
def index(request):
    nilai = 100000
    hasil = ppn11persen(nilai)
    return HttpResponse(hasil)

    # context = {
    #     'name' : 'rizki'
    # }
    # return render(request, 'index.html', context)

def tambah_user(request):
    return render(request, 'tambah-user.html')

def post_user(request):
    userid = request.POST['userid']
    username = request.POST['username']
    password = request.POST['password']
    password2 = request.POST['password2']

    if Users.objects.filter(userid=userid).exists():
        messages.error(request, 'userid sudah digunakan')
        return redirect(request.META.get('HTTP_REFERER', '/'))
    else:
        if password == password2: 
            tambah_user = Users(
                userid = userid,
                username = username,
                password = password
            )
            tambah_user.save()
            messages.success(request, 'berhasil tambah user')
        else:
            messages.error(request, 'password tidak sama!')
    return redirect(request.META.get('HTTP_REFERER', '/'))

def master_user(request):
    data_user = Users.objects.all()
    context = {
        'data_user': data_user
    }
    return render(request, 'master-user.html', context)

    # json_data_user = json.dumps(list(data_user.values()))
    # return HttpResponse(json_data_user)

def update_user(request, userid):
    data_user = Users.objects.get(userid=userid)
    context = {
        'data_user': data_user
    }

    return render(request, 'update-user.html', context)

def postupdate_user(request):
    #ambil data
    userid = request.POST['userid']
    username = request.POST['username']
    password = request.POST['password']
    password2 = request.POST['password2']

    # proses update
    user = Users.objects.get(userid=userid)
    if password == password2:
        user.username = username
        user.password = password
        user.save()
        messages.success(request, 'berhasil update user')
    else:
        messages.error(request, 'password tidak sama!')
    return redirect(request.META.get('HTTP_REFERER', '/'))

def delete_user(request, userid):
    Users.objects.get(userid=userid).delete()
    messages.success(request, 'berhasil hapus user')
    return redirect(request.META.get('HTTP_REFERER', '/'))

