from django.shortcuts import render

# Create your views here.

def dexprop(request):
	return render(request,'dexprop.html')

def bimbingan(request):
	contex = {
		'no' : '1',
		'tanggal' : '12 Juli 1996',
		'hasil' : 'Teruskan lh'
	}

	return render(request, 'bimprop.html',contex)

def sidang(request):
	return render(request, 'sidprop.html')
