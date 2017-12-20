from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Mahasiswa(models.Model):
    akunMhs = models.OneToOneField(User,
                                   on_delete=models.CASCADE,
                                   related_name='akunMhs')
    npm = models.CharField(max_length=14, unique=True)
    posisi = models.CharField(max_length=1, default='A')

    def __str__(self):
        return self.akunMhs.username


class Dosen(models.Model):
    akunDsn = models.OneToOneField(User,
                                   on_delete=models.CASCADE,
                                   related_name="akunDsn")
    nidn = models.CharField(max_length=10, unique=True)
    gelar = models.CharField(max_length=25,
                             default="M. Kom"
                             )

    def __str__(self):
        return self.akunDsn.first_name + " " + self.akunDsn.last_name
