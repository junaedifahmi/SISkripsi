# from django.db import models
# from base.models import *
#
# #Create your models here.
#
# class Proposal(models.Model):
#     """docstring for Proposal"""
#     mhs = models.OneToOneField(Mahasiswa,
#                                on_delete=models.CASCADE()
#                                )
#     judul = models.CharField(max_length=100,unique=True)
#     ringkasan = models.CharField(max_length=5000)
#     keyword = models.CharField(max_length=100)
#     dospem = models.ForeignKey(Dosen)
#
#     def __str__(self):
#         print(self.judul + ' ' + self.npm.nama)
#
#
# class BimbinganProposal(Bimbingan):
#     proposal = models.OneToOneField(Proposal,on_delete=models.CASCADE())
#
#     def __str__(self):
#         print("proposal atas nama "+ self.proposal.mhs.nama + " dengan judul " + self.proposal.judul)
#
# class SidangProposal(Sidang):
#     proposal =models.OneToOneField(Proposal,
#                                    on_delete=models.DO_NOTHING())
#     def __str__(self):
#         print("Sidang untuk ",self.proposal.mhs.akun.nama," akan dilaksanakan pada tanggal ",self.tgl)
