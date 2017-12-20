# coding=utf-8

from proposal.models import BimbinganProposal, SeminarProposal, Proposal
from base.models import Dosen
from django import forms


class Tanggal(forms.widgets.DateInput):
	input_type = 'date'


class Texta(forms.widgets.Textarea):
	attrs = {
		'cols': 60,
		'rows': 1,
		'style': 'resize:none;'
		}

class FormProposal(forms.ModelForm):

	dospem = forms.ModelChoiceField(queryset=Dosen.objects.all(), to_field_name="nidn")
	class Meta:
		model = Proposal
		fields = ['judul', 'katakunci', 'ringkasan', 'dospem', 'akun']
		widgets = {
				'judul': forms.Textarea(attrs={'cols': 60, 'rows': 1, 'style': 'resize:none;'}),
				'katakunci': forms.Textarea(attrs={'cols': 60, 'rows': 1, 'style': 'resize:none;'}),
				'ringkasan': forms.Textarea(attrs={'cols': 60, 'rows': 1, 'style': 'resize:none;'}),
				'dospem': forms.HiddenInput,
				'akun': forms.HiddenInput
			}


class FormBimbingan(forms.ModelForm):
	class Meta:
		model = BimbinganProposal
		fields = ['hasil', 'tanggal', 'proposal']
		widgets = {
			'hasil': forms.Textarea(attrs={'cols': 60, 'rows': 1, 'style': 'resize:none;'}),
			'tanggal': Tanggal()
		}


class FormSeminar(forms.ModelForm):
	class Meta:
		model = SeminarProposal
		fields = ['fileProposal', 'proposal']