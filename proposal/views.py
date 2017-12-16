# coding=utf-8
from django.shortcuts import render, redirect
from proposal.models import *
from base.models import Dosen
from django.views.generic import View
# Create your views here.

app_name = 'proposal'


def index(request):
    """
    fungsi ini untuk menampilkan tampilan awal dari proposal
    :param request:
    :return:
    """

    context = {
        'dosen': Dosen.objects.all().order_by('akunDsn__first_name')
    }
    try:
        prop = Proposal.objects.get(akun=request.user)
        context.update({
            'prop': prop
        })
    except Proposal.DoesNotExist:
        pass
    finally:
        return render(request, 'dexprop.html', context)


def bimbingan(request):
    """
    FUngsi untuk menampilkan catatan bimbingan
    :param request:
    :return:
    """

    context = {}
    try:
        prop = Proposal.objects.get(akun=request.user)
        try:
            p = BimbinganProposal.objects.filter(proposal=prop)
            context.update({
                'a': p
            })

        except BimbinganProposal.DoesNotExist:
            context.update({'error': "anda belum melakukan bimbingan samsek"})
    except Proposal.DoesNotExist:
        context.update({'error': "anda belum membuat proposal"})
    finally:
        return render(request, 'bimprop.html', context)


def sidang(request):
    """
    Fungsi untuk menampilkan informasi tentang sidang proposal
    :param request:
    :return:
    """

    context = {}
    try:
        prop = Proposal.objects.get(akun=request.user)
        try:
            p = BimbinganProposal.objects.filter(proposal=prop).count()
            print(p)
            if p > 3:
                p = 'checked'
            else:
                p= ' '
            context.update(
                {
                    'a': p
                }
            )
        except BimbinganProposal.DoesNotExist:
            context.update({'error': "anda belum melakukan bimbingan samsek"})
    except Proposal.DoesNotExist:
        context.update({'error': "anda belum membuat proposal"})
    finally:
        return render(request, 'sidprop.html', context)

########################################################
################### form handler #######################
########################################################

def tambah(request):
    """
    fungsi ini untuk menambahkan bimbingan,
    harusnya ini diisi setiap kali melakukan bimbingan
    :param request:
    :return:
    """
    if request.method == 'POST':
        o = BimbinganProposal()
        o.hasil = request.POST.get('hasil')
        o.tanggal = request.POST.get('tanggal')
        o.proposal = Proposal.objects.get(akun=request.user)
        o.save()

    return redirect('proposal:bimbingan')


def edit(request):
    """
    fungsi ini untuk mengedit identitas proposal
    :param request:
    :return:
    """
    if request.method == 'POST':
        dosen = Dosen.objects.get(nidn=request.POST.get('dosepem'))
        print(request.POST.get('judul'))
        print(request.POST.get('dosepem'))

        o = Proposal()
        o.judul = request.POST.get('judul')
        o.katakunci = request.POST.get('keywords')
        o.ringkasan = request.POST.get('ringkasan')
        o.dospem = dosen
        o.akun = request.user
        o.save()

    return redirect('proposal:index')
