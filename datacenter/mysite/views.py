from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	myname="森"
	return render(request,"index.html",locals())

# Create your views here.
