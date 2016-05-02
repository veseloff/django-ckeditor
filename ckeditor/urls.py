from django.conf.urls import patterns, url

from .views import upload, browse

urlpatterns = [
    url(r'^upload/', upload, name='ckeditor_upload'),
    url(r'^browse/', browse, name='ckeditor_browse'),
]
