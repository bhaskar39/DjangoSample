from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app2.models import post_data
from django.utils import timezone

def index(request):
	q=post_data(user='kishore',email='kishorekumarnetala@gmail.com',post_head='multiple_db',description='success second db',post_date=timezone.now())
	q.save(using='db2')
	return HttpResponse("hello")