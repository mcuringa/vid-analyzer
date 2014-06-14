from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'vidan.views.home'),
    url(r'^home$', 'vidan.views.home'),
    url(r'^upload$', 'vidan.views.upload'),
    url(r'^login$', 'vidan.views.login_user'),
    url(r'^dataset$', 'vidan.views.dataset'),
    url(r'^results$', 'vidan.views.results'),
)
