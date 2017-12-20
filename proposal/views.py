# coding=utf-8
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from proposal.models import *
from proposal.forms import *
from django.views.generic import View
from django.views.generic.edit import UpdateView

# Create your views here.

app_name = 'proposal'

class Index(View):
	template_name = 'indexproposal.html'
	context = {}

	def get(self, request):
		form = FormProposal(None)
		self.context.update({
			'user': Mahasiswa.objects.get(akunMhs=request.user),
			'form': form
			})
		try:
			prop = Proposal.objects.get(akun=request.user)
			self.context.update({
				'prop': prop
				})
		except Proposal.DoesNotExist:
			pass
		finally:
			return render(request, self.template_name, self.context)

	def post(self, request):
		form = FormProposal(request.POST)
		if form.is_valid():
			o = form.save(commit=False)
			o.dospem = Dosen.objects.get(nidn=request.POST['dospem'])
			o.akun = request.user
			o.save()
		else:
			pass

		return redirect('proposal:index')



class Bimbingan(View):
	"""
	Kelas ini dibuat untuk memberikan hasil ke dalam Bimbingan
	"""
	template_name = "bimbinganproposal.html"
	form = FormBimbingan
	content = {}

	def get(self, request):
		"""
		untuk menampilkan hasil semua bimbingan
		:param request:
		:return:
		"""
		form = FormBimbingan(None)
		self.content.update(dict(form=form))
		try:
			proposal = Proposal.objects.get(akun=request.user)
			try:
				hasilbimbingan = BimbinganProposal.objects.filter(proposal=proposal)
				self.content.update(dict(hasil=hasilbimbingan))
			except BimbinganProposal.DoesNotExist:
				self.content.update(dict(error_Bimbingan="Anda belum bimbingan samsek"))
		except Proposal.DoesNotExist:
			self.content.update(dict(error_proposal="Anda belum membuat proposal"))
		finally:
			return render(request, self.template_name, self.content)

	def post(self, request):
		"""
		fungsi untuk menambah bimbingan ke dalam database
		:param request:
		:return:
		"""
		form = FormBimbingan(request.POST)
		if form.is_valid():
			a = form.save(commit=False)
			a.proposal = Proposal.objects.get(akun=request.user)
			a.save()
		else:
			self.content.update(dict(error_post="Form yang anda buat tidak valid, periksa kembali form anda"))

		return redirect('proposal:bimbingan')


class Seminar(View):
	"""
		Ini untuk seminar proposal, dari informasi sampe daftar
	"""

	template_name = "sidangproposal.html"
	content = {
		'ada': False
		}
	seminar = SeminarProposal

	def get(self, request):
		"""
			untuk menampilkan form pendaftaran
		:param request:
		:return:
		"""
		form = FormSeminar(None)
		self.content.update(dict(form=form))
		try:
			prop = Proposal.objects.get(akun=request.user)
			try:
				p = BimbinganProposal.objects.filter(proposal=prop).count()
				# print(p)
				if p > 3:
					masabimbingan = 'checked'
				else:
					masabimbingan = ' '
				self.content.update(dict(masabimbingan=masabimbingan))
			except BimbinganProposal.DoesNotExist:
				self.content.update(dict(error="anda belum melakukan bimbingan samsek"))
		except Proposal.DoesNotExist:
			self.content.update(dict(error="anda belum membuat proposal"))
		finally:
			return render(request, 'sidangproposal.html', self.content)

	def post(self, request):
		"""
		untuk daftar seminar gitu loh
		:param request:
		:return: hasil
		"""
		form = FormSeminar(request.POST, request.FILES)
		if form.is_valid():
			o = form.save(commit=False)
			o.proposal = Proposal.objects.get(akun=request.user)
			o.save()
			self.content.update({'ada': True})
			return redirect('proposal:seminar')
		else:
			self.content.update(dict(error_post="Form yang anda buat tidak valid, periksa kembali form anda"))
			return render(request, self.template_name, self.content)
		return redirect('proposal:index')


class Edit(UpdateView):
	model = Proposal
	fields = ['judul', 'katakunci', 'ringkasan', 'dospem']
	template_name = 'indexproposal.html'
	success_url = reverse_lazy('proposal:index')

