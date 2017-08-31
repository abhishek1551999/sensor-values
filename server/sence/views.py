# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse,JsonResponse
import json
from django.http import StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

data = []
@csrf_exempt
def index(request):
    if request.method=='POST':
        
        data1 = request.POST['temperature']
        data.append(data1)
        print(data)
        #return render(request,"index.html",{'value':data})
        return JsonResponse(data,safe = False)
    if request.method == 'GET':
        #data = request.GET['temperature']
        return JsonResponse(data,safe = False)
    return HttpResponse(request,data)
'''
from django.shortcuts import render

def server(request):
    if request.method == 'POSt'
    data1 = request.POST['temperature']
    data2 = request.POST['humidity']

    return render(request,"server.html",{'reading1':data1,'reading2':data2})
# Create your views here.'''
