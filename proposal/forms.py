# coding=utf-8

from proposal.models import BimbinganProposal
from django import forms

class Bimbingan(forms.ModelForm):

    class Meta:
        model = BimbinganProposal

        fields = ['tanggal', 'hasil', 'proposal']
