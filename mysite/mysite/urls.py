from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^statics/(?P<path>.*)$','django.views.static.serve',{'document_root': settings.STATIC_ROOT}),
    url(r'^authen/',include('authen.urls')),
]
