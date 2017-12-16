from django.db import models


# Create your models here.


class User(models.Model):
    email = models.EmailField(max_length=150, primary_key=True)
    pw = models.CharField(max_length=255)


class Mahasiswa(models.Model):
    akunMhs = models.OneToOneField(User,
                                   on_delete=models.CASCADE,
                                   related_name='akunMhs')
    nama = models.CharField(max_length=100)
    npm = models.CharField(max_length=14, unique=True)


class Dosen(models.Model):
    akunDsn = models.OneToOneField(User,
                                   on_delete=models.CASCADE,
                                   related_name="akunDsn")
    nama = models.CharField(max_length=100)
    nidn = models.CharField(max_length=10, unique=True)
