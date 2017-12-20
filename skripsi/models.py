from django.db import models
from django.utils import timezone
from proposal.models import Proposal, Dosen


class Skripsi(models.Model):
	proposal = models.OneToOneField(Proposal, on_delete=models.CASCADE)
	pembimbing1 = models.ForeignKey(Dosen, on_delete=models.DO_NOTHING, related_name="dospem1")
	pembimbing2 = models.ForeignKey(Dosen, on_delete=models.DO_NOTHING, related_name="dospem2")


class BimbinganSkripsi(models.Model):

	tanggal = models.DateField(default=timezone.now)
	hasil = models.TextField(max_length=1000)

	def __str__(self):
		return self.hasil