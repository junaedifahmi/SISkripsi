from django.shortcuts import render

# Create your views here.

def dexskripsi(request):
	return render(request,'dexskripsi.html')

def bimbingan(request):
	return render(request, 'bimskrip.html')

def sidang(request):
	return render(request, 'sidskrip.html')
