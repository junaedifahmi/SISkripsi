from django.shortcuts import render

# Create your views here.
def dex(request):
	return render(request,'dex.html')

def home(request):
	return render(request,'home.html')
