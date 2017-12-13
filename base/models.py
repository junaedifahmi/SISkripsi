# from django.db import models
#
# # Create your models here.
# class User(models.Model):
#     email = models.EmailField(primary_key=True)
#     pw = models.CharField(max_length=255)
#     phone = models.CharField(max_length=14)
#     nama = models.CharField(max_length=50)
#
# class Mahasiswa(User):
#     """docstring for Mahasiswa"""
#     npm = models.CharField(max_length=16,primary_key=True)
#     akun = models.OneToOneField(User,
#                                 on_delete=models.CASCADE())
#
#     def __str__(self):
#         print(self.npm + ' ' + self.nama)
#
#
# class Dosen(User):
#     """docstring for Dosen"""
#     nidn = models.CharField(max_length=10,primary_key=True)
#     akun = models.OneToOneField(User,on_delete=models.CASCADE())
#
#     def __str__(self):
#         print("Nama dosen : "+self.email.nama)
#
#
# class Sidang(models.Model):
#     """docstring for Sidang"""
#     mhs = models.ForeignKey(Mahasiswa,
#                             on_delete=models.CASCADE())
#     tgl = models.DateField()
#     def __str__(self):
#         print(self.mhs.akun.nama + ' ' + self.tgl)
#
# class Bimbingan(models.Model):
#     """docstring for Bimbingan"""
#     tanggal = models.DateField()
#     hasil = models.TextField()
#
#     def __str__(self):
#         print(self.tanggal + ' ' + self.hasil)
