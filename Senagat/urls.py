from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('administrator/', include('administrator.urls')),
    path('api_v1/', include('api_v1.urls')),
    path('captcha/', include('captcha.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
