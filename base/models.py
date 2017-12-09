from django.db import models

# Create your models here.
class Mahasiswa(models.Model):
	"""docstring for Mahasiswa"""
	npm = models.CharField(max_length=16)
	nama = models.CharField(max_length=50)

	def __str__(self):
		print(self.npm + ' ' + self.nama)

class Dosen(models.Model):
	"""docstring for Dosen"""
	nidn = models.CharField(max_length=10)
	nama = models.CharField(max_length=35)

class Proposal(models.Model):
	"""docstring for Proposal"""
	judul = models.CharField(max_length=100)
	ringkasan = models.CharField(max_length=5000)
	keyword = models.CharField(max_length=100)

	def __str__(self):
		print(self.npm + ' ' + self.nama)
		
class Skripsi(models.Model):
	"""docstring for Skripsi"""
	npm = models.CharField(max_length=16)
	nama = models.CharField(max_length=50)

	def __str__(self):
		print(self.npm + ' ' + self.nama)

class Sidang(models.Model):
	"""docstring for Sidang"""
	npm = models.CharField(max_length=16)
	nama = models.CharField(max_length=50)

	def __str__(self):
		print(self.npm + ' ' + self.nama)

class Bimbingan(models.Model):
	"""docstring for Bimbingan"""

	npm = models.CharField(max_length=16)
	nama = models.CharField(max_length=50)

	def __str__(self):
		print(self.npm + ' ' + self.nama)