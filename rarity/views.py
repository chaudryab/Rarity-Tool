from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
import requests 
import pandas as pd

def index(request):
    return redirect('/rarity_tool/index')
