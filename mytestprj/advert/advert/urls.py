import filebrowser
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from filebrowser.sites import site as filebrowser_site

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('admin/filebrowser/', filebrowser_site.urls),
    path('api/content/', include('api.urls')),
    path('api/users/', include('authentication.urls')),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)