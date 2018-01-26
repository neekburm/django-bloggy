"""bloggy_project URL Configuration
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.static import serve
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
]
