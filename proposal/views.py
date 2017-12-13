from django.shortcuts import render
from django.views.generic import *

# Create your views here.

class IndexProp(ListView):
    template_name = 'dexprop.html'

    def get_queryset(self):
        pass

class Bimbingan(View):
    template_name = 'bimprop.html'

    def get(self, request):
        return render(request,self.template_name)

    def get_queryset(self):
        pass

class SidangProposal(View):
    template_name = 'sidprop.html'
