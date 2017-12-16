from django.conf.urls import include, url
from base.views import *

app_name = 'base'


urlpatterns = [
    url(r'^$', dex, name='dex'),
    url(r'^home/$', home, name='home'),
    url(r'^login', login, name='login')
]
