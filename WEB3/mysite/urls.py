from django.conf.urls import url
#from django.contrib import admin
from .views import home, register
from . import views 


app_name = 'mysite'


urlpatterns = [
    url(r'^$', home),

    #url(r'^register/', register),

    ##url(r'^$', views.home, name='home')
    ##url(r'^$', Home.as_view(), name='home')



url(r'^$', views.index, name='index'),
url(r'^register/$', views.register, name='register'),
#url(r'^$', views.home, name='home'),

url(r'^login_user/$', views.login_user, name='login_user'),

#url(r'^login/$', auth_views.login),
#url(r'^logout/$', auth_views.logout),



]