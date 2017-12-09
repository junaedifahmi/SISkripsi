from django.conf.urls import include, url
from base.views import *

urlpatterns = [
    url(r'^$', dex,name='dex'),
    url(r'^home/$',home,name='home')
]
