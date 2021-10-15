import json
from django.http import HttpResponse, request
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
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

def low_rarity_tool(request):
    data = Rarity.objects.filter(first_sale='Y').order_by('price')[:40]
    return render(request, 'low_rarity_tool.html',{'data':data})

@csrf_exempt
def low_first_url(request):
    counter = int(request.POST.get('counter'))
    data = Rarity.objects.filter(first_sale='Y').order_by('price')[counter:counter+40] 
    if data.count() > 0:
        data = json.loads(serializers.serialize('json', data))
        return JsonResponse({'data':data},safe=False)
    else:
        return JsonResponse({'data':[]},safe=False) 
    
def high_rarity_tool(request):
    data = Rarity.objects.filter(first_sale='Y').order_by('-price')[:40]
    return render(request, 'high_rarity_tool.html',{'data':data})

@csrf_exempt
def high_first_url(request):
    counter = int(request.POST.get('counter'))
    data = Rarity.objects.filter(first_sale='Y').order_by('-price')[counter:counter+40] 
    if data.count() > 0:
        data = json.loads(serializers.serialize('json', data))
        return JsonResponse({'data':data},safe=False)
    else:
        return JsonResponse({'data':[]},safe=False) 

myarray=[]
P_min = 0
P_max = 0
R_min = 0
R_max = 0
@csrf_exempt
def filter(request):
    global myarray
    global P_min
    global P_max
    global R_min
    global R_max
    if request.method == 'POST':
        p_min = request.POST['p_min']
        p_max = request.POST['p_max']
        r_min = request.POST['r_min']
        r_max = request.POST['r_max']
        P_min = p_min 
        P_max = p_max 
        R_min = r_min  
        R_max = r_max 
        if (p_min != '' and p_max != '') and (r_min != '' and r_max != ''):
            p = Rarity.objects.filter(first_sale='Y',price__gte=p_min,price__lte=p_max)[:40]
            ids = []
            for d in p:
                ids.append(d.id)
            data = Rarity.objects.filter(id__in=ids,counter__gte=r_min,counter__lte=r_max)
            for f in data:
                myarray.append(f.id)
            return render(request,'filter.html',{'data':data,'p_min':p_min,'p_max':p_max,'r_min':r_min,'r_max':r_max})
        elif p_min != '' and p_max != '':
            data = Rarity.objects.filter(first_sale='Y',price__gte=p_min,price__lte=p_max)[:40]
            for f in data:
                myarray.append(f.id)
            return render(request,'filter.html',{'data':data,'p_min':p_min,'p_max':p_max,'r_min':r_min,'r_max':r_max})
        elif r_min != '' and r_max != '':
            data = Rarity.objects.filter(first_sale='Y',counter__gte=r_min,counter__lte=r_max)[:40]
            for f in data:
                myarray.append(f.id)
            return render(request,'filter.html',{'data':data,'p_min':p_min,'p_max':p_max,'r_min':r_min,'r_max':r_max})
        else:
            return redirect('rarity_tool')
            
@csrf_exempt
def filter_url(request):
    counter = int(request.POST.get('counter'))
    p_min = float(request.POST.get('p_min')) if request.POST.get('p_min') != '' else request.POST.get('p_min')
    p_max = float(request.POST.get('p_max')) if request.POST.get('p_max') != '' else request.POST.get('p_max')
    r_min = int(request.POST.get('r_min')) if request.POST.get('r_min') != '' else request.POST.get('r_min')
    r_max = int(request.POST.get('r_max')) if request.POST.get('r_max') != '' else request.POST.get('r_max')
    if (p_min != '' and p_max != '') and (r_min != '' and r_max != ''):
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
    elif p_min != '' and p_max != '':
        data = Rarity.objects.filter(first_sale='Y',price__gte=p_min,price__lte=p_max)[counter:counter+40]
        if data.count() > 0:
            data = json.loads(serializers.serialize('json', data))
            return JsonResponse({'data':data},safe=False)
        else:
            return JsonResponse({'data':[]},safe=False)
    elif r_min != '' and r_max != '':
        data = Rarity.objects.filter(first_sale='Y',counter__gte=r_min,counter__lte=r_max)[counter:counter+40]
        if data.count() > 0:
            data = json.loads(serializers.serialize('json', data))
            return JsonResponse({'data':data},safe=False)
        else:
            return JsonResponse({'data':[]},safe=False)

@csrf_exempt
def rarity_filter(request):
    data = Rarity.objects.filter(id__in=myarray)[:40]
    p_min = P_min 
    p_max = P_max 
    r_min = R_min  
    r_max = R_max 
    return render(request,'filter.html',{'data':data,'p_min':p_min,'p_max':p_max,'r_min':r_min,'r_max':r_max})

@csrf_exempt
def low_filter(request):
    data = Rarity.objects.filter(id__in=myarray).order_by('price')[:40]
    p_min = P_min 
    p_max = P_max 
    r_min = R_min  
    r_max = R_max 
    return render(request,'low_filter.html',{'data':data,'p_min':p_min,'p_max':p_max,'r_min':r_min,'r_max':r_max})

@csrf_exempt
def low_filter_url(request):
    counter = int(request.POST.get('counter'))
    p_min = float(request.POST.get('p_min')) if request.POST.get('p_min') != '' else request.POST.get('p_min')
    p_max = float(request.POST.get('p_max')) if request.POST.get('p_max') != '' else request.POST.get('p_max')
    r_min = int(request.POST.get('r_min')) if request.POST.get('r_min') != '' else request.POST.get('r_min')
    r_max = int(request.POST.get('r_max')) if request.POST.get('r_max') != '' else request.POST.get('r_max')
    if (p_min != '' and p_max != '') and (r_min != '' and r_max != ''):
        p = Rarity.objects.filter(first_sale='Y',price__gte=p_min,price__lte=p_max).order_by('price')[counter:counter+40]
        ids = []
        for d in p:
            ids.append(d.id)
        data = Rarity.objects.filter(id__in=ids,counter__gte=r_min,counter__lte=r_max).order_by('price')
        if data.count() > 0:
            data = json.loads(serializers.serialize('json', data))
            return JsonResponse({'data':data},safe=False)
        else:
            return JsonResponse({'data':[]},safe=False)
    elif p_min != '' and p_max != '':
        data = Rarity.objects.filter(first_sale='Y',price__gte=p_min,price__lte=p_max).order_by('price')[counter:counter+40]
        if data.count() > 0:
            data = json.loads(serializers.serialize('json', data))
            return JsonResponse({'data':data},safe=False)
        else:
            return JsonResponse({'data':[]},safe=False)
    elif r_min != '' and r_max != '':
        data = Rarity.objects.filter(first_sale='Y',counter__gte=r_min,counter__lte=r_max).order_by('price')[counter:counter+40]
        if data.count() > 0:
            data = json.loads(serializers.serialize('json', data))
            return JsonResponse({'data':data},safe=False)
        else:
            return JsonResponse({'data':[]},safe=False)

@csrf_exempt
def high_filter(request):
    data = Rarity.objects.filter(id__in=myarray).order_by('-price')[:40]
    p_min = P_min 
    p_max = P_max 
    r_min = R_min  
    r_max = R_max 
    return render(request,'high_filter.html',{'data':data,'p_min':p_min,'p_max':p_max,'r_min':r_min,'r_max':r_max})          

@csrf_exempt
def high_filter_url(request):
    counter = int(request.POST.get('counter'))
    p_min = float(request.POST.get('p_min')) if request.POST.get('p_min') != '' else request.POST.get('p_min')
    p_max = float(request.POST.get('p_max')) if request.POST.get('p_max') != '' else request.POST.get('p_max')
    r_min = int(request.POST.get('r_min')) if request.POST.get('r_min') != '' else request.POST.get('r_min')
    r_max = int(request.POST.get('r_max')) if request.POST.get('r_max') != '' else request.POST.get('r_max')
    if (p_min != '' and p_max != '') and (r_min != '' and r_max != ''):
        p = Rarity.objects.filter(first_sale='Y',price__gte=p_min,price__lte=p_max).order_by('-price')[counter:counter+40]
        ids = []
        for d in p:
            ids.append(d.id)
        data = Rarity.objects.filter(id__in=ids,counter__gte=r_min,counter__lte=r_max).order_by('-price')
        if data.count() > 0:
            data = json.loads(serializers.serialize('json', data))
            return JsonResponse({'data':data},safe=False)
        else:
            return JsonResponse({'data':[]},safe=False)
    elif p_min != '' and p_max != '':
        data = Rarity.objects.filter(first_sale='Y',price__gte=p_min,price__lte=p_max).order_by('-price')[counter:counter+40]
        if data.count() > 0:
            data = json.loads(serializers.serialize('json', data))
            return JsonResponse({'data':data},safe=False)
        else:
            return JsonResponse({'data':[]},safe=False)
    elif r_min != '' and r_max != '':
        data = Rarity.objects.filter(first_sale='Y',counter__gte=r_min,counter__lte=r_max).order_by('-price')[counter:counter+40]
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
    
def low_all_rarity_tool(request):
    data = Rarity.objects.all().order_by('price')[:40]
    return render(request, 'low_all_rarity_tool.html',{'data':data})

@csrf_exempt
def low_all_url(request):
    counter = int(request.POST.get('counter'))
    data = Rarity.objects.all().order_by('price')[counter:counter+40] 
    if data.count() > 0:
        data = json.loads(serializers.serialize('json', data))
        return JsonResponse({'data':data},safe=False)
    else:
        return JsonResponse({'data':[]},safe=False) 
    
    
def high_all_rarity_tool(request):
    data = Rarity.objects.all().order_by('-price')[:40]
    return render(request, 'high_all_rarity_tool.html',{'data':data})

@csrf_exempt
def high_all_url(request):
    counter = int(request.POST.get('counter'))
    data = Rarity.objects.all().order_by('-price')[counter:counter+40] 
    if data.count() > 0:
        data = json.loads(serializers.serialize('json', data))
        return JsonResponse({'data':data},safe=False)
    else:
        return JsonResponse({'data':[]},safe=False) 
    
@csrf_exempt
def filter_all(request):
    global myarray
    global P_min
    global P_max
    global R_min
    global R_max
    if request.method == 'POST':
        p_min = request.POST['p_min']
        p_max = request.POST['p_max']
        r_min = request.POST['r_min']
        r_max = request.POST['r_max']
        P_min = p_min 
        P_max = p_max 
        R_min = r_min  
        R_max = r_max 
        if (p_min != '' and p_max != '') and (r_min != '' and r_max != ''):
            p = Rarity.objects.filter(price__gte=p_min,price__lte=p_max)[:40]
            ids = []
            for d in p:
                ids.append(d.id)
            data = Rarity.objects.filter(id__in=ids,counter__gte=r_min,counter__lte=r_max)
            for f in data:
                myarray.append(f.id)
            return render(request,'filter_all.html',{'data':data,'p_min':p_min,'p_max':p_max,'r_min':r_min,'r_max':r_max})
        elif p_min != '' and p_max != '':
            data = Rarity.objects.filter(price__gte=p_min,price__lte=p_max)[:40]
            for f in data:
                myarray.append(f.id)
            return render(request,'filter_all.html',{'data':data,'p_min':p_min,'p_max':p_max,'r_min':r_min,'r_max':r_max})
        elif r_min != '' and r_max != '':
            data = Rarity.objects.filter(counter__gte=r_min,counter__lte=r_max)[:40]
            for f in data:
                myarray.append(f.id)
            return render(request,'filter_all.html',{'data':data,'p_min':p_min,'p_max':p_max,'r_min':r_min,'r_max':r_max})
        else:
            return redirect('all_rarity_tool')
    
@csrf_exempt
def filter_url_all(request):
    counter = int(request.POST.get('counter'))
    p_min = float(request.POST.get('p_min')) if request.POST.get('p_min') != '' else request.POST.get('p_min')
    p_max = float(request.POST.get('p_max')) if request.POST.get('p_max') != '' else request.POST.get('p_max')
    r_min = int(request.POST.get('r_min')) if request.POST.get('r_min') != '' else request.POST.get('r_min')
    r_max = int(request.POST.get('r_max')) if request.POST.get('r_max') != '' else request.POST.get('r_max')
    if (p_min != '' and p_max != '') and (r_min != '' and r_max != ''):
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
    elif p_min != '' and p_max != '':
        data = Rarity.objects.filter(price__gte=p_min,price__lte=p_max)[counter:counter+40]
        if data.count() > 0:
            data = json.loads(serializers.serialize('json', data))
            return JsonResponse({'data':data},safe=False)
        else:
            return JsonResponse({'data':[]},safe=False)
    elif r_min != '' and r_max != '':
        data = Rarity.objects.filter(counter__gte=r_min,counter__lte=r_max)[counter:counter+40]
        if data.count() > 0:
            data = json.loads(serializers.serialize('json', data))
            return JsonResponse({'data':data},safe=False)
        else:
            return JsonResponse({'data':[]},safe=False)

@csrf_exempt
def rarity_filter_all(request):
    data = Rarity.objects.filter(id__in=myarray)[:40]
    p_min = P_min 
    p_max = P_max 
    r_min = R_min  
    r_max = R_max 
    return render(request,'filter_all.html',{'data':data,'p_min':p_min,'p_max':p_max,'r_min':r_min,'r_max':r_max})

@csrf_exempt
def low_filter_all(request):
    data = Rarity.objects.filter(id__in=myarray).order_by('price')[:40]
    p_min = P_min 
    p_max = P_max 
    r_min = R_min  
    r_max = R_max 
    return render(request,'low_filter_all.html',{'data':data,'p_min':p_min,'p_max':p_max,'r_min':r_min,'r_max':r_max})

@csrf_exempt
def low_filter_url_all(request):
    counter = int(request.POST.get('counter'))
    p_min = float(request.POST.get('p_min')) if request.POST.get('p_min') != '' else request.POST.get('p_min')
    p_max = float(request.POST.get('p_max')) if request.POST.get('p_max') != '' else request.POST.get('p_max')
    r_min = int(request.POST.get('r_min')) if request.POST.get('r_min') != '' else request.POST.get('r_min')
    r_max = int(request.POST.get('r_max')) if request.POST.get('r_max') != '' else request.POST.get('r_max')
    if (p_min != '' and p_max != '') and (r_min != '' and r_max != ''):
        p = Rarity.objects.filter(price__gte=p_min,price__lte=p_max).order_by('price')[counter:counter+40]
        ids = []
        for d in p:
            ids.append(d.id)
        data = Rarity.objects.filter(id__in=ids,counter__gte=r_min,counter__lte=r_max).order_by('price')
        if data.count() > 0:
            data = json.loads(serializers.serialize('json', data))
            return JsonResponse({'data':data},safe=False)
        else:
            return JsonResponse({'data':[]},safe=False)
    elif p_min != '' and p_max != '':
        data = Rarity.objects.filter(price__gte=p_min,price__lte=p_max).order_by('price')[counter:counter+40]
        if data.count() > 0:
            data = json.loads(serializers.serialize('json', data))
            return JsonResponse({'data':data},safe=False)
        else:
            return JsonResponse({'data':[]},safe=False)
    elif r_min != '' and r_max != '':
        data = Rarity.objects.filter(counter__gte=r_min,counter__lte=r_max).order_by('price')[counter:counter+40]
        if data.count() > 0:
            data = json.loads(serializers.serialize('json', data))
            return JsonResponse({'data':data},safe=False)
        else:
            return JsonResponse({'data':[]},safe=False)
        
@csrf_exempt
def high_filter_all(request):
    data = Rarity.objects.filter(id__in=myarray).order_by('-price')[:40]
    p_min = P_min 
    p_max = P_max 
    r_min = R_min  
    r_max = R_max 
    return render(request,'high_filter_all.html',{'data':data,'p_min':p_min,'p_max':p_max,'r_min':r_min,'r_max':r_max})

@csrf_exempt
def high_filter_url_all(request):
    counter = int(request.POST.get('counter'))
    p_min = float(request.POST.get('p_min')) if request.POST.get('p_min') != '' else request.POST.get('p_min')
    p_max = float(request.POST.get('p_max')) if request.POST.get('p_max') != '' else request.POST.get('p_max')
    r_min = int(request.POST.get('r_min')) if request.POST.get('r_min') != '' else request.POST.get('r_min')
    r_max = int(request.POST.get('r_max')) if request.POST.get('r_max') != '' else request.POST.get('r_max')
    if (p_min != '' and p_max != '') and (r_min != '' and r_max != ''):
        p = Rarity.objects.filter(price__gte=p_min,price__lte=p_max).order_by('-price')[counter:counter+40]
        ids = []
        for d in p:
            ids.append(d.id)
        data = Rarity.objects.filter(id__in=ids,counter__gte=r_min,counter__lte=r_max).order_by('-price')
        if data.count() > 0:
            data = json.loads(serializers.serialize('json', data))
            return JsonResponse({'data':data},safe=False)
        else:
            return JsonResponse({'data':[]},safe=False)
    elif p_min != '' and p_max != '':
        data = Rarity.objects.filter(price__gte=p_min,price__lte=p_max).order_by('-price')[counter:counter+40]
        if data.count() > 0:
            data = json.loads(serializers.serialize('json', data))
            return JsonResponse({'data':data},safe=False)
        else:
            return JsonResponse({'data':[]},safe=False)
    elif r_min != '' and r_max != '':
        data = Rarity.objects.filter(counter__gte=r_min,counter__lte=r_max).order_by('-price')[counter:counter+40]
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

def low_secondary_rarity_tool(request):
    data = Rarity.objects.filter(first_sale='N').order_by('price')[:40]
    return render(request, 'low_secondary_rarity_tool.html',{'data':data})

@csrf_exempt
def low_secondary_url(request):
    counter = int(request.POST.get('counter'))
    data = Rarity.objects.filter(first_sale='N').order_by('price')[counter:counter+40] 
    if data.count() > 0:
        data = json.loads(serializers.serialize('json', data))
        return JsonResponse({'data':data},safe=False)
    else:
        return JsonResponse({'data':[]},safe=False) 
    
def high_secondary_rarity_tool(request):
    data = Rarity.objects.filter(first_sale='N').order_by('-price')[:40]
    return render(request, 'high_secondary_rarity_tool.html',{'data':data})

@csrf_exempt
def high_secondary_url(request):
    counter = int(request.POST.get('counter'))
    data = Rarity.objects.filter(first_sale='N').order_by('-price')[counter:counter+40] 
    if data.count() > 0:
        data = json.loads(serializers.serialize('json', data))
        return JsonResponse({'data':data},safe=False)
    else:
        return JsonResponse({'data':[]},safe=False) 

@csrf_exempt
def secondary_filter(request):
    global myarray
    global P_min
    global P_max
    global R_min
    global R_max
    if request.method == 'POST':
        p_min = request.POST['p_min']
        p_max = request.POST['p_max']
        r_min = request.POST['r_min']
        r_max = request.POST['r_max']
        P_min = p_min 
        P_max = p_max 
        R_min = r_min  
        R_max = r_max
        if (p_min != '' and p_max != '') and (r_min != '' and r_max != ''):
            p = Rarity.objects.filter(first_sale='N',price__gte=p_min,price__lte=p_max)[:40]
            ids = []
            for d in p:
                ids.append(d.id)
            data = Rarity.objects.filter(id__in=ids,counter__gte=r_min,counter__lte=r_max)
            for f in data:
                myarray.append(f.id)
            return render(request,'secondary_filter.html',{'data':data,'p_min':p_min,'p_max':p_max,'r_min':r_min,'r_max':r_max})
        elif p_min != '' and p_max != '':
            data = Rarity.objects.filter(first_sale='N',price__gte=p_min,price__lte=p_max)[:40]
            for f in data:
                myarray.append(f.id)
            return render(request,'secondary_filter.html',{'data':data,'p_min':p_min,'p_max':p_max,'r_min':r_min,'r_max':r_max})
        elif r_min != '' and r_max != '':
            data = Rarity.objects.filter(first_sale='N',counter__gte=r_min,counter__lte=r_max)[:40]
            for f in data:
                myarray.append(f.id)
            return render(request,'secondary_filter.html',{'data':data,'p_min':p_min,'p_max':p_max,'r_min':r_min,'r_max':r_max})
        else:
            return redirect('secondary_rarity_tool')
    
@csrf_exempt
def secondary_filter_url(request):
    counter = int(request.POST.get('counter'))
    p_min = float(request.POST.get('p_min')) if request.POST.get('p_min') != '' else request.POST.get('p_min')
    p_max = float(request.POST.get('p_max')) if request.POST.get('p_max') != '' else request.POST.get('p_max')
    r_min = int(request.POST.get('r_min')) if request.POST.get('r_min') != '' else request.POST.get('r_min')
    r_max = int(request.POST.get('r_max')) if request.POST.get('r_max') != '' else request.POST.get('r_max')
    if (p_min != '' and p_max != '') and (r_min != '' and r_max != ''):
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
    elif p_min != '' and p_max != '':
        data = Rarity.objects.filter(first_sale='N',price__gte=p_min,price__lte=p_max)[counter:counter+40]
        if data.count() > 0:
            data = json.loads(serializers.serialize('json', data))
            return JsonResponse({'data':data},safe=False)
        else:
            return JsonResponse({'data':[]},safe=False)
    elif r_min != '' and r_max != '':
        data = Rarity.objects.filter(first_sale='N',counter__gte=r_min,counter__lte=r_max)[counter:counter+40]
        if data.count() > 0:
            data = json.loads(serializers.serialize('json', data))
            return JsonResponse({'data':data},safe=False)
        else:
            return JsonResponse({'data':[]},safe=False)

@csrf_exempt
def secondary_filter_all(request):
    data = Rarity.objects.filter(id__in=myarray)[:40]
    p_min = P_min 
    p_max = P_max 
    r_min = R_min  
    r_max = R_max 
    return render(request,'secondary_filter.html',{'data':data,'p_min':p_min,'p_max':p_max,'r_min':r_min,'r_max':r_max})

@csrf_exempt
def low_secondary_filter(request):
    data = Rarity.objects.filter(id__in=myarray).order_by('price')[:40]
    p_min = P_min 
    p_max = P_max 
    r_min = R_min  
    r_max = R_max 
    return render(request,'low_secondary_filter.html',{'data':data,'p_min':p_min,'p_max':p_max,'r_min':r_min,'r_max':r_max})

@csrf_exempt
def low_secondary_filter_url(request):
    counter = int(request.POST.get('counter'))
    p_min = float(request.POST.get('p_min')) if request.POST.get('p_min') != '' else request.POST.get('p_min')
    p_max = float(request.POST.get('p_max')) if request.POST.get('p_max') != '' else request.POST.get('p_max')
    r_min = int(request.POST.get('r_min')) if request.POST.get('r_min') != '' else request.POST.get('r_min')
    r_max = int(request.POST.get('r_max')) if request.POST.get('r_max') != '' else request.POST.get('r_max')
    if (p_min != '' and p_max != '') and (r_min != '' and r_max != ''):
        p = Rarity.objects.filter(first_sale='N',price__gte=p_min,price__lte=p_max).order_by('price')[counter:counter+40]
        ids = []
        for d in p:
            ids.append(d.id)
        data = Rarity.objects.filter(id__in=ids,counter__gte=r_min,counter__lte=r_max).order_by('price')
        if data.count() > 0:
            data = json.loads(serializers.serialize('json', data))
            return JsonResponse({'data':data},safe=False)
        else:
            return JsonResponse({'data':[]},safe=False)
    elif p_min != '' and p_max != '':
        data = Rarity.objects.filter(first_sale='N',price__gte=p_min,price__lte=p_max).order_by('price')[counter:counter+40]
        if data.count() > 0:
            data = json.loads(serializers.serialize('json', data))
            return JsonResponse({'data':data},safe=False)
        else:
            return JsonResponse({'data':[]},safe=False)
    elif r_min != '' and r_max != '':
        data = Rarity.objects.filter(first_sale='N',counter__gte=r_min,counter__lte=r_max).order_by('price')[counter:counter+40]
        if data.count() > 0:
            data = json.loads(serializers.serialize('json', data))
            return JsonResponse({'data':data},safe=False)
        else:
            return JsonResponse({'data':[]},safe=False)

@csrf_exempt
def high_secondary_filter(request):
    data = Rarity.objects.filter(id__in=myarray).order_by('-price')[:40]
    p_min = P_min 
    p_max = P_max 
    r_min = R_min  
    r_max = R_max 
    return render(request,'high_secondary_filter.html',{'data':data,'p_min':p_min,'p_max':p_max,'r_min':r_min,'r_max':r_max})

@csrf_exempt
def high_secondary_filter_url(request):
    counter = int(request.POST.get('counter'))
    p_min = float(request.POST.get('p_min')) if request.POST.get('p_min') != '' else request.POST.get('p_min')
    p_max = float(request.POST.get('p_max')) if request.POST.get('p_max') != '' else request.POST.get('p_max')
    r_min = int(request.POST.get('r_min')) if request.POST.get('r_min') != '' else request.POST.get('r_min')
    r_max = int(request.POST.get('r_max')) if request.POST.get('r_max') != '' else request.POST.get('r_max')
    if (p_min != '' and p_max != '') and (r_min != '' and r_max != ''):
        p = Rarity.objects.filter(first_sale='N',price__gte=p_min,price__lte=p_max).order_by('-price')[counter:counter+40]
        ids = []
        for d in p:
            ids.append(d.id)
        data = Rarity.objects.filter(id__in=ids,counter__gte=r_min,counter__lte=r_max).order_by('-price')
        if data.count() > 0:
            data = json.loads(serializers.serialize('json', data))
            return JsonResponse({'data':data},safe=False)
        else:
            return JsonResponse({'data':[]},safe=False)
    elif p_min != '' and p_max != '':
        data = Rarity.objects.filter(first_sale='N',price__gte=p_min,price__lte=p_max).order_by('-price')[counter:counter+40]
        if data.count() > 0:
            data = json.loads(serializers.serialize('json', data))
            return JsonResponse({'data':data},safe=False)
        else:
            return JsonResponse({'data':[]},safe=False)
    elif r_min != '' and r_max != '':
        data = Rarity.objects.filter(first_sale='N',counter__gte=r_min,counter__lte=r_max).order_by('-price')[counter:counter+40]
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
        
        
        

