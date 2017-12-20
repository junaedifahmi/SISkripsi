from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView
from skripsi.forms import *
from skripsi.models import *

# Create your views here.

def dexskripsi(request):
	return render(request ,'indexskripsi.html')

def bimbingan(request):
	return render(request ,'bimbinganskripsi.html')

def sidang(request):
	return render(request ,'sidangskripsi.html')

class HasilBimbingan(DetailView):
	template_name = "bimbingan/detailBimbingan.html"


class ListBimbingan(CreateView):
	template_name = "bimbingan/ListBimbingan.html"
	model = BimbinganSkripsi
	form_class = TambahBimbingan
