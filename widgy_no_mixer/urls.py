from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.conf import settings

from widgy_no_mixer.widgy_site import site as widgy_site

urlpatterns = patterns('',
    # url('^sitemap.xml$', TemplateView.as_view(template_name='sitemap.xml', content_type='application/xml'),
    ('^admin/widgy/', include(widgy_site.urls)),
    # Examples:
    # url(r'^$', '{{ project_name }}.views.home', name='home'),
    # url(r'^{{ project_name }}/', include('{{ project_name }}.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    )
