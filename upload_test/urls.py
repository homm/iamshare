from django.conf.urls import patterns, include, url

from imageshare import views


urlpatterns = patterns('',
    url(r'^$', views.UploadView.as_view()),
)
