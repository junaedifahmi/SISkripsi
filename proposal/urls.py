# coding=utf-8


"""
xcfhjk
"""


from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from proposal.views import *

app_name = 'proposal'

urlpatterns = [
    url(r'^$', login_required(Index.as_view()), name='index'),
    url(r'^edit/(?P<pk>[0-9]+)/$', Edit.as_view(), name='edit'),
    url(r'^bimbingan/$', login_required(Bimbingan.as_view()), name='bimbingan'),
    url(r'^seminar', login_required(Seminar.as_view()), name='seminar'),
    ]
