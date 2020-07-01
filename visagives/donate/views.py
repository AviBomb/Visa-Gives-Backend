from django.shortcuts import render
from django.http import HttpResponse
# from callapi import callApi
import sys
sys.path.insert(1, '../utilities.py')
from utilities import callApi

def index(request):
    callApi()
    return HttpResponse("Hello, world. You're at the polls index.")
