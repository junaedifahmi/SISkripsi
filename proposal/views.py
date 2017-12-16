# coding=utf-8
from django.shortcuts import render, redirect

from proposal.models import *
# Create your views here.

app_name = 'proposal'

def index(request):
    """
    fungsi ini untuk menampilkan tampilan awal dari proposal
    :param request:
    :return:
    """
    if request.method =='POST':
        mhs = Mahasiswa.objects.get(akunMhs=request.session['user'])
        prop = Proposal
        prop.judul = request.POST.get('judul')
        prop.katakunci = request.POST.get('keywords')
        prop.ringkasan = request.POST.get('ringkasan')
        prop.dospem = request.POST.get('dospem')
        mhs.prop_set.add(prop)
    else:
        prop = Proposal.objects.prefetch_related(request.session['user'])
        context = {
            'judul' : prop.judul,
            'keywords' : prop.katakunci,
            'ringkasan' : prop.ringkasan
        }


    return render(request, 'dexprop.html', context)


def bimbingan(request):
    """
    FUngsi untuk menampilkan catatan bimbingan
    :param request:
    :return:
    """
    uid = request.session['user']
    print(uid)

    p = BimbinganProposal.objects.all()
    return render(request, 'bimprop.html', {'a': p})


def sidang(request):
    """
    Fungsi untuk menampilkan informasi tentang sidang proposal
    :param request:
    :return:
    """
    context = {

    }

    return render(request, 'sidprop.html', context)


def tambah(request):
    """
    fungsi ini untuk menambahkan bimbingan,
    harusnya ini diisi setiap kali melakukan bimbingan
    :param request:
    :return:
    """
    if request.method == 'POST':
        o = BimbinganProposal
        o.hasil = request.POST.get('hasil')
        o.tanggal = request.POST.get('tanggal')
        o.save()

    return redirect('proposal:bimbingan')


def edit(request):
    """
    fungsi ini untuk mengedit identitas proposal
    :param request:
    :return:
    """
    if request.method == 'POST':
        o = Proposal()
        o.judul = request.POST.get('judul')
        o.ringkasan = request.POST.get('ringkasan')
        o.katakunci = request.POST.get('keywords')
        o.save()

    return redirect('proposal:index')
