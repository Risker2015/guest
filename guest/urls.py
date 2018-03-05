#__*__coding:utf-8__*__
from django.conf.urls import include, url
from django.contrib import admin
from sign import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'guest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^sign/', include('sign.urls')),
]
