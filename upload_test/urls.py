from django.conf.urls import patterns, include, url

from imageshare import views


urlpatterns = patterns('',
    url(r'^$', views.UploadView.as_view()),
    url(r'^view/(?P<pk>[a-z]{6})/$', views.ImageView.as_view(), name='detail'),
)
