from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
        url(r'^$', 'cms.views.mostrar'),
        url(r'(.+)/(.+)', 'cms.views.guardar'),
        url(r'(.+)', 'cms.views.nueva'),
        url(r'(.*)/(.*)', 'cms.views.Error404'),
)
