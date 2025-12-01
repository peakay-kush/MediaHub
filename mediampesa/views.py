from os import times
import requests # we use this lib. in python to interact with API's 
from django.shortcuts import render, redirect
from django.db.models.expressions import result
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse # json format for our results as well queries 
from .models import Transactions
import base64 # encryption at a script one 
from datetime import datetime
import json
from django.core.mail import send_mail
from django.core.paginator import Paginator
from dotenv import load_dotenv

load_dotenv() # making our settings config available to our view files 


# Create your views here.
# helper class for transaction security credentials  :: Auth token :: - access to use the API routes from daraja mpesa 
# authorization 
class MpesaPassword:
    pass

# get the access token from mpesa 
def generate_access_token():
    pass

# index page for transactions 
def index(request):
    pass

# this will execute an stk push on request 
@csrf_exempt  
def stk_push(request):
    pass

# this function maps my callback url that will receive the result body of a transaction/ payment attempt 
@csrf_exempt
def callback(request): 
    pass

# waiting page 
def waiting_page(request, transaction_id):
    pass

# check and update status pending -complete 
def check_status(request, transaction_id):
    pass

# helper functions - render payment successful , render payment failed , render payment cancelled 
def payment_success(request):
    pass

def payment_failed(request):
    pass

def payment_cancelled(request):
    pass