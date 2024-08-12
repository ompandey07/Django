from django.shortcuts import render , redirect
from django.http import HttpResponse
from database.models import userdata


def mainpage (request):
    if request.method == 'GET':
        data = userdata.objects.all()
        return render (request , 'index.html' , {'data' : data})
    
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        db = userdata  (username = username , email = email)
        db.save()
        return redirect ('mainpage')
