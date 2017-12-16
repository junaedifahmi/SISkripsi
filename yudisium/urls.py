from django.conf.urls import include, url
from yudisium.views import *

app_name = 'yudisium'

urlpatterns = [
    url(r'^$', revisi, name='revisi'),
    url(r'^jurnal/$', jurnal, name='jurnal'),
    url(r'^sidang/$', sidang, name='sidang'),
    url(r'^wisuda/$', wisuda, name='wisuda'),

]
