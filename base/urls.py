from django.conf.urls import url
from base.views import *
from django.contrib.auth.decorators import login_required


app_name = 'base'


urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
    url(r'^home/$', login_required(Home.as_view()), name='home'),
    url(r'^logout/$', logout_view, name='logout'),
]
