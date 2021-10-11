import json
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render
import requests 
from .models import *
import pandas as pd
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers



def index(request):
    data = Rarity.objects.all()[:40]
    return render(request, 'index.html',{'data':data})


@csrf_exempt
def index_url(request):
    counter = int(request.POST.get('counter'))
    data = Rarity.objects.all()[counter:counter+40] 
    if data.count() > 0:
        data = json.loads(serializers.serialize('json', data))
        return JsonResponse({'data':data},safe=False)
    else:
        return JsonResponse({'data':[]},safe=False)



def first_rarity_tools(request):
    data = Rarity.objects.filter(first_sale='Y')[:40]
    return render(request, 'first_rarity_tools.html',{'data':data})

@csrf_exempt
def first_url(request):
    counter = int(request.POST.get('counter'))
    data = Rarity.objects.filter(first_sale='Y')[counter:counter+40] 
    if data.count() > 0:
        data = json.loads(serializers.serialize('json', data))
        return JsonResponse({'data':data},safe=False)
    else:
        return JsonResponse({'data':[]},safe=False) 

@csrf_exempt
def price(request):
    if request.method == 'POST':
        min = request.POST['min']
        max = request.POST['max']
        data = Rarity.objects.filter(price__gte=min,price__lte=max)[:40]
        return render(request, 'price_rarity_tools.html',{'data':data,'min':min,'max':max})

@csrf_exempt
def price_url(request):
    counter = int(request.POST.get('counter'))
    min = float(request.POST.get('min'))
    max = float(request.POST.get('max'))
    data = Rarity.objects.filter(price__gte=min,price__lte=max)[counter:counter+40]
    if data.count() > 0:
        data = json.loads(serializers.serialize('json', data))
        return JsonResponse({'data':data},safe=False)
    else:
        return JsonResponse({'data':[]},safe=False)

@csrf_exempt
def rank(request):
    if request.method == 'POST':
        min = request.POST['min']
        max = request.POST['max']
        data = Rarity.objects.filter(counter__gte=min,counter__lte=max)[:40]
        return render(request, 'rank_rarity_tools.html',{'data':data,'min':min,'max':max})
   
@csrf_exempt
def rank_url(request):
    counter = int(request.POST.get('counter'))
    min = int(request.POST.get('min'))
    max = int(request.POST.get('max'))
    data = Rarity.objects.filter(counter__gte=min,counter__lte=max)[counter:counter+40]
    if data.count() > 0:
        data = json.loads(serializers.serialize('json', data))
        return JsonResponse({'data':data},safe=False)
    else:
        return JsonResponse({'data':[]},safe=False)


def get_data_excel():
    csv_url='https://docs.google.com/spreadsheets/d/1eAEMSjrpsP6VbfYZ6g8FvFkopQ4wRSYjowNoxsk7W5c/export?format=csv&id=1eAEMSjrpsP6VbfYZ6g8FvFkopQ4wRSYjowNoxsk7W5c&gid=1995217609'
    res=requests.get(url=csv_url)
    open('2nd_page_data.csv', 'wb').write(res.content)
    csv_rows = pd.read_csv("2nd_page_data.csv")
    del_rarity = Rarity.objects.all()
    del_rarity.delete()
    for i, j in csv_rows.iterrows():
        rarity = Rarity(counter=i+1,name= j[11],true_owner=j[16],first_sale=j[18],price=j[17],image_url=j[10],url=j[9])
        rarity.save()

def get_data(request):
    csv_url='https://docs.google.com/spreadsheets/d/1eAEMSjrpsP6VbfYZ6g8FvFkopQ4wRSYjowNoxsk7W5c/export?format=csv&id=1eAEMSjrpsP6VbfYZ6g8FvFkopQ4wRSYjowNoxsk7W5c&gid=1995217609'
    res=requests.get(url=csv_url)
    open('2nd_page_data.csv', 'wb').write(res.content)
    csv_rows = pd.read_csv("2nd_page_data.csv")
    del_rarity = Rarity.objects.all()
    del_rarity.delete()
    print("start")
    count = 1
    for i, j in csv_rows.iterrows():
        rarity = Rarity(counter=i+1,name= j[11],true_owner=j[16],first_sale=j[18],price=j[17],image_url=j[10],url=j[9])
        rarity.save()
        count = count + 1
        print(count)
    print("done")
    return HttpResponse(1)
