from django.shortcuts import render

# Create your views here.
def revisi(request):
	return render(request,'revisi.html')

def jurnal(request):
	return render(request,'jurnal.html')

def sidang(request):
	return render(request,'sidang.html')

def wisuda(request):
	return render(request,'wisuda.html')