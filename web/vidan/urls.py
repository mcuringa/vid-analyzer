from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    

    url(r'^$', 'vidan.views.home', name='home'),
    url(r'^home$', 'vidan.views.home', name='home'),
    url(r'^upload$', 'vidan.views.upload', name='upload'),


    #url(r'^admin/', include(admin.site.urls)),


)
