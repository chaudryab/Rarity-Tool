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
    return render(request, 'index.html')

def kings_tom(request):
    return render(request, 'kings_tom.html')


#---------------- First Sale -----------------
def rarity_tool(request):
    data = Rarity.objects.filter(first_sale='Y')[:40]
    return render(request, 'rarity_tool.html',{'data':data})

@csrf_exempt
def first_url(request):
    counter = int(request.POST.get('counter'))
    data = Rarity.objects.filter(first_sale='Y')[counter:counter+40] 
    if data.count() > 0:
        data = json.loads(serializers.serialize('json', data))
        return JsonResponse({'data':data},safe=False)
    else:
        return JsonResponse({'data':[]},safe=False) 

def des_rarity_tool(request):
    data = Rarity.objects.filter(first_sale='Y').order_by('-id')[:40]
    return render(request, 'des_rarity_tool.html',{'data':data})

@csrf_exempt
def des_first_url(request):
    counter = int(request.POST.get('counter'))
    data = Rarity.objects.filter(first_sale='Y').order_by('-id')[counter:counter+40] 
    if data.count() > 0:
        data = json.loads(serializers.serialize('json', data))
        return JsonResponse({'data':data},safe=False)
    else:
        return JsonResponse({'data':[]},safe=False) 

@csrf_exempt
def filter(request):
    if request.method == 'POST':
        p_min = request.POST['p_min']
        p_max = request.POST['p_max']
        r_min = request.POST['r_min']
        r_max = request.POST['r_max']
        p = Rarity.objects.filter(first_sale='Y',price__gte=p_min,price__lte=p_max)[:40]
        ids = []
        for d in p:
            ids.append(d.id)
        data = Rarity.objects.filter(id__in=ids,counter__gte=r_min,counter__lte=r_max)
        return render(request,'filter.html',{'data':data,'p_min':p_min,'p_max':p_max,'r_min':r_min,'r_max':r_max})

    
@csrf_exempt
def filter_url(request):
    counter = int(request.POST.get('counter'))
    p_min = float(request.POST.get('p_min'))
    p_max = float(request.POST.get('p_max'))
    r_min = int(request.POST.get('r_min'))
    r_max = int(request.POST.get('r_max'))
    p = Rarity.objects.filter(first_sale='Y',price__gte=p_min,price__lte=p_max)[counter:counter+40]
    ids = []
    for d in p:
        ids.append(d.id)
    data = Rarity.objects.filter(id__in=ids,counter__gte=r_min,counter__lte=r_max)
    if data.count() > 0:
        data = json.loads(serializers.serialize('json', data))
        return JsonResponse({'data':data},safe=False)
    else:
        return JsonResponse({'data':[]},safe=False)


#---------------- ALL -----------------

def all_rarity_tool(request):
    data = Rarity.objects.all()[:40]
    return render(request, 'all_rarity_tool.html',{'data':data})

@csrf_exempt
def all_url(request):
    counter = int(request.POST.get('counter'))
    data = Rarity.objects.all()[counter:counter+40] 
    if data.count() > 0:
        data = json.loads(serializers.serialize('json', data))
        return JsonResponse({'data':data},safe=False)
    else:
        return JsonResponse({'data':[]},safe=False) 
    
def des_all_rarity_tool(request):
    data = Rarity.objects.all().order_by('-id')[:40]
    return render(request, 'des_all_rarity_tool.html',{'data':data})

@csrf_exempt
def des_all_url(request):
    counter = int(request.POST.get('counter'))
    data = Rarity.objects.all().order_by('-id')[counter:counter+40] 
    if data.count() > 0:
        data = json.loads(serializers.serialize('json', data))
        return JsonResponse({'data':data},safe=False)
    else:
        return JsonResponse({'data':[]},safe=False) 
    
@csrf_exempt
def filter_all(request):
    if request.method == 'POST':
        p_min = request.POST['p_min']
        p_max = request.POST['p_max']
        r_min = request.POST['r_min']
        r_max = request.POST['r_max']
        p = Rarity.objects.filter(price__gte=p_min,price__lte=p_max)[:40]
        ids = []
        for d in p:
            ids.append(d.id)
        data = Rarity.objects.filter(id__in=ids,counter__gte=r_min,counter__lte=r_max)
        return render(request,'filter_all.html',{'data':data,'p_min':p_min,'p_max':p_max,'r_min':r_min,'r_max':r_max})

    
@csrf_exempt
def filter_url_all(request):
    counter = int(request.POST.get('counter'))
    p_min = float(request.POST.get('p_min'))
    p_max = float(request.POST.get('p_max'))
    r_min = int(request.POST.get('r_min'))
    r_max = int(request.POST.get('r_max'))
    p = Rarity.objects.filter(price__gte=p_min,price__lte=p_max)[counter:counter+40]
    ids = []
    for d in p:
        ids.append(d.id)
    data = Rarity.objects.filter(id__in=ids,counter__gte=r_min,counter__lte=r_max)
    if data.count() > 0:
        data = json.loads(serializers.serialize('json', data))
        return JsonResponse({'data':data},safe=False)
    else:
        return JsonResponse({'data':[]},safe=False)



#---------------- Second Sale -----------------
def secondary_rarity_tool(request):
    data = Rarity.objects.filter(first_sale='N')[:40]
    return render(request, 'secondary_rarity_tool.html',{'data':data})

@csrf_exempt
def second_url(request):
    counter = int(request.POST.get('counter'))
    data = Rarity.objects.filter(first_sale='N')[counter:counter+40] 
    if data.count() > 0:
        data = json.loads(serializers.serialize('json', data))
        return JsonResponse({'data':data},safe=False)
    else:
        return JsonResponse({'data':[]},safe=False) 

def des_secondary_rarity_tool(request):
    data = Rarity.objects.filter(first_sale='N').order_by('-id')[:40]
    return render(request, 'des_secondary_rarity_tool.html',{'data':data})

@csrf_exempt
def des_secondary_url(request):
    counter = int(request.POST.get('counter'))
    data = Rarity.objects.filter(first_sale='N').order_by('-id')[counter:counter+40] 
    if data.count() > 0:
        data = json.loads(serializers.serialize('json', data))
        return JsonResponse({'data':data},safe=False)
    else:
        return JsonResponse({'data':[]},safe=False) 


@csrf_exempt
def secondary_filter(request):
    if request.method == 'POST':
        p_min = request.POST['p_min']
        p_max = request.POST['p_max']
        r_min = request.POST['r_min']
        r_max = request.POST['r_max']
        p = Rarity.objects.filter(first_sale='Y',price__gte=p_min,price__lte=p_max)[:40]
        ids = []
        for d in p:
            ids.append(d.id)
        data = Rarity.objects.filter(id__in=ids,counter__gte=r_min,counter__lte=r_max)
        return render(request,'secondary_filter.html',{'data':data,'p_min':p_min,'p_max':p_max,'r_min':r_min,'r_max':r_max})

    
@csrf_exempt
def secondary_filter_url(request):
    counter = int(request.POST.get('counter'))
    p_min = float(request.POST.get('p_min'))
    p_max = float(request.POST.get('p_max'))
    r_min = int(request.POST.get('r_min'))
    r_max = int(request.POST.get('r_max'))
    p = Rarity.objects.filter(first_sale='N',price__gte=p_min,price__lte=p_max)[counter:counter+40]
    ids = []
    for d in p:
        ids.append(d.id)
    data = Rarity.objects.filter(id__in=ids,counter__gte=r_min,counter__lte=r_max)
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
        
        

