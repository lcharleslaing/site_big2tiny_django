from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from site_big2tiny import settings

urlpatterns = [
                  path('', include('home.urls')),
                  path('iam/', include('iam.urls')),
                  path('authors/', include('authors.urls')),
                  path('admin/', admin.site.urls),
                  path('accounts/', include('account.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
