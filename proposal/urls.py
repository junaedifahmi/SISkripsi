from django.conf.urls import include, url

from proposal.views import *

urlpatterns = [
    url(r'^$',IndexProp.as_view(),name='proposal'),
    url(r'^bimbingan/',Bimbingan.as_view(),name='bimbingan'),
    url(r'^sidang',SidangProposal.as_view(),name='sidang')
]
