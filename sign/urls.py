from django.conf.urls import include, url
from django.contrib import admin
from sign import views
from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'guest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^index/$', views.index),
    url(r'^accounts/login/$',views.index),
    url(r'^login_action/$', views.login_action),
    url(r'^event_manage/$',views.event_manage),
    url(r'^guest_manage/$', views.guest_manage),
    url(r'^search_name/$',views.search_name),
    url(r'^sign_index/(?P<event_id>[0-9]+)/$',views.sign_index),
]
