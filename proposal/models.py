from django.utils import timezone

from django.db import models as md

from base.models import *


# Create your models here.


class Proposal(md.Model):
    """
        Ini adalah model untuk identitas proposal
    """

    akun = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name="mhsAkun")
    judul = models.TextField(max_length=500, unique=True)
    katakunci = models.TextField(max_length=500)
    ringkasan = models.TextField(max_length=1000)
    dospem = models.ForeignKey(Dosen, on_delete=models.DO_NOTHING)

    def __str__(self):
        return "Proposal untuk " + self.akun.username


class BimbinganProposal(md.Model):
    proposal = models.ForeignKey(Proposal,
                                 on_delete=models.CASCADE,
                                 related_name="propID")
    tanggal = md.DateField(default=timezone.now)
    hasil = md.TextField(max_length=500)

    def __str__(self):
        return "Bimbingan untuk " + self.proposal.judul


class SeminarProposal(md.Model):

    #diisi oleh mahasiswa
    fileProposal = models.FileField()

    #diisi oleh sistem
    proposal = models.OneToOneField(Proposal,
                                    on_delete=models.CASCADE,
                                    related_name="propSid",
                                    unique=True)
    masabimbingan = models.BooleanField()

    #disi oleh admin
    tanggal = models.DateField(default=timezone.now, blank=True)
    tempat = models.CharField(max_length=30, blank=True)

    #diisi oleh dosen pembimbing
    dospemsetuju = models.BooleanField(default=False, blank=True)

    #diisi oleh kaprodi
    penguji1 = models.ForeignKey(Dosen,
                                 on_delete=models.CASCADE,
                                 related_name="penguji1",
                                 blank=True)
    penguji2 = models.ForeignKey(Dosen,
                                 on_delete=models.CASCADE,
                                 related_name="penguji2",
                                 blank=True)



    def __str__(self):
        return "Sidang untuk " + self.proposal.judul
