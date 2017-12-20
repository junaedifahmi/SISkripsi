from django import forms
from skripsi.models import *


class TambahBimbingan(forms.ModelForm):
	class Meta:
		model = BimbinganSkripsi
		fields = ['tanggal', 'hasil']