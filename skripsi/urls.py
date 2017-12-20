from django.conf.urls import include, url
from skripsi.views import *

app_name = 'skripsi'

urlpatterns = [
    url(r'^$', dexskripsi, name='dexskripsi'),
    url(r'^bimbingan/', ListBimbingan.as_view(), name='bimbingan'),
    url(r'^sidang', sidang, name='sidang')
]
