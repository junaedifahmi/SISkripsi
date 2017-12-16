from django.utils import timezone

from django.db import models as md

from base.models import *


# Create your models here.


class Proposal(md.Model):
    """
        Ini adalah model untuk identitas proposal
    """

    akun = models.OneToOneField(Mahasiswa,
                                on_delete=models.DO_NOTHING,
                                related_name="mhsAkun")
    judul = models.TextField(max_length=500)
    katakunci = models.TextField(max_length=500)
    ringkasan = models.TextField(max_length=1000)
    dospem = models.ForeignKey(Dosen, on_delete=models.DO_NOTHING)

    def __str__(self):
        return "Proposal untuk " + self.akun.nama


class BimbinganProposal(md.Model):
    proposal = models.ForeignKey(Proposal,
                                 on_delete=models.CASCADE,
                                 related_name="propID")
    tanggal = md.DateField(default=timezone.now)
    hasil = md.TextField(max_length=500)

    def __str__(self):
        return "Bimbingan untuk " + self.proposal.judul


class Sidang(md.Model):
    proposal = models.OneToOneField(Proposal,
                                    on_delete=models.CASCADE,
                                    related_name="propSid")
    tanggal = models.DateField(default=timezone.now)
    dospem = models.BooleanField(default=False)

    def __str__(self):
        return "Sidang untuk "+ self.proposal.judul
